import win32api
import win32gui
import win32con
import win32process
import time
import os


class Win32Helper:

    @classmethod
    def start_application(cls, path_or_name):
        try:
            # create process return process handle, thread handle, process id, thread id
            result = win32process.CreateProcess(None, "Notepad", None, None, 0, 0, None, None, win32process.STARTUPINFO())
        except Exception as e:
            message = "fail to start application: {0} with error: {1}".format(path_or_name, str(e))
            print(message)
            raise
        return result

    @classmethod
    def quit_application(cls, process_handle=None, process_name=None):
        try:
            if process_handle:
                win32process.TerminateProcess(process_handle, 0)
            elif process_name:
                os.system("taskkill /F /IM %s" % process_name)
            else:
                raise Exception("no parameter")
        except Exception as e:
            message = "fail to close application: {0} with error: {1}".format(process_handle, str(e))
            print(message)
            raise

    @classmethod
    def execute_command(cls, command):
        try:
            # available to start app or visit url as well
            result = win32api.ShellExecute(0, "open", command, "", "", 1)
        except Exception as e:
            message = "fail to execute: {0} with error: {1}".format(command, str(e))
            print(message)
            raise
        return result

    @classmethod
    def find_window(cls, window_name):
        try:
            duration = 10
            handle = False
            while duration:
                handle = win32gui.FindWindow(0, window_name)
                if handle != 0:
                    break
                duration -= 1
                time.sleep(1)
            return handle
        except Exception as e:
            message = "fail to find window by name: {0} with error: {1}".format(window_name, str(e))
            print(message)
            raise

    @classmethod
    def find_window_by_partial_title(cls, partial_title):
        try:
            duration = 10
            handle = False
            while duration:
                for hwnd, window_text, window_class in cls.get_all_windows():
                    if window_text.find(partial_title) >= 0:
                        handle = hwnd
                        break
                duration -= 1
                time.sleep(1)
            return handle
        except Exception as e:
            message = "fail to find window by partial text: {0} with error: {1}".format(partial_title, str(e))
            print(message)
            raise

    @classmethod
    def close_window(cls, window_text, partial=False, handle=None):
        try:
            if handle:
                result = win32gui.SendMessage(handle, win32con.WM_CLOSE, 0, 0)
            else:
                if partial:
                    handle = cls.find_window_by_partial_title(window_text)
                else:
                    handle = cls.find_window(window_text)
                result = win32gui.SendMessage(handle, win32con.WM_CLOSE, 0, 0)
            return result
        except Exception as e:
            message = "fail to close window by window text: {0} with error: {1}".format(window_text, str(e))
            print(message)
            raise

    @classmethod
    def send_keyboard_signal(cls, window_handle, key):
        assert window_handle, "window handle cannot be None"
        assert key, "key of keyboard cannot be None"
        self.Keys = {"Tab": win32con.VK_TAB,
                     "Down": win32con.VK_DOWN,
                     "Enter": win32con.VK_RETURN,
                     "Up": win32con.VK_UP
                     }
        win32api.SendMessage(window_handle, win32con.WM_KEYDOWN, cls.Keys[key], 0)

    @classmethod
    def get_all_windows(cls):
        all_windows = []
        win32gui.EnumWindows(cls._window_enumeration_handler, all_windows)
        return all_windows

    @classmethod
    def _window_enumeration_handler(cls, hwnd, window_list):
        window_list.append((hwnd,
                           win32gui.GetWindowText(hwnd),
                           win32gui.GetClassName(hwnd)))
