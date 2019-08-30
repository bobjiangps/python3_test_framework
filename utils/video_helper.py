import os
import platform as pf
import subprocess


class VideoHelper:

    def __init__(self, out_file="output.mp4", frame_rate=30, mac_video_device="avfoundation", mac_video_index=1, win_video_device="gdigrab", win_video_area="desktop"):
        self.out_file = out_file
        if os.path.exists(self.out_file):
            print("remove existent out_file")
            os.remove(self.out_file)
        self.frame_rate = frame_rate
        self.mac_video_device = mac_video_device
        self.mac_video_index = mac_video_index
        self.win_video_device = win_video_device
        self.win_video_area = win_video_area
        self.platform = self.get_system_type()
        self.process = None

    @staticmethod
    def get_system_type():
        platform = pf.platform().lower()
        if platform.find("windows") >= 0:
            return "win"
        elif platform.find("darwin") >= 0:
            return "mac"
        else:
            return "linux"

    def start_recording_screen(self):
        if self.platform == "mac":
            cmd = "ffmpeg -f %s -i %d -r %d %s" % (self.mac_video_device, self.mac_video_index, self.frame_rate, self.out_file)
        elif self.platform == "win":
            cmd = "ffmpeg -f %s -i %s -r %d %s" % (self.win_video_device, self.win_video_area, self.frame_rate, self.out_file)
        else:
            raise Exception("system type not support yet")
        # self.process = subprocess.Popen(cmd, shell=True)
        self.process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def stop_recording_screen(self):
        if self.process:
            # self.process.terminate()
            self.process.stdin.write('q'.encode("GBK"))
            self.process.communicate()
