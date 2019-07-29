from configuration.config import LoadConfig
from utils.selenium_helper import SeleniumHelper
from utils.appium_helper import AppiumHelper
from py.xml import html
import pytest
import os
import datetime
import json


total_sum = pass_sum = fail_sum = skip_sum = 0
module_case = {}


#@pytest.hookimpl(hookwrapper=True, tryfirst=True)
@pytest.hookimpl(hookwrapper=True)
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    stat_file = os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "test_reports", "stat.json")
    global total_sum
    global pass_sum
    global fail_sum
    global skip_sum
    global module_case
    outcome = yield
    rep = outcome.get_result()
    test_file = item.function.__module__.split(".")[-1]
    if test_file not in module_case.keys():
        module_case[test_file] = {}
    rep.description = str(item.function.__doc__)
    setattr(item, "rep_" + rep.when, rep)
    if rep.when == "setup" and rep.skipped:
        test_method = rep.nodeid.split("::")[-1]
        if test_method not in module_case[test_file]:
            total_sum += 1
            skip_sum += 1
        module_case[test_file][test_method] = "skip"
    if rep.when == "call":
        print("%s: Case Duration: %ss ...%s" % (rep.nodeid.split("::")[-1], str(round(rep.duration, 2)), rep.outcome))
        test_method = rep.nodeid.split("::")[-1]
        if rep.passed:
            if test_method not in module_case[test_file]:
                total_sum += 1
                pass_sum += 1
            else:
                pass_sum += 1
                fail_sum -= 1
            module_case[test_file][test_method] = "pass"
        elif rep.failed:
            if test_method not in module_case[test_file]:
                total_sum += 1
                fail_sum += 1
            module_case[test_file][test_method] = "fail"
            config = LoadConfig.load_config()
            if config["report"]["ui_test"]:
                screen_folder_path = os.path.join(os.getcwd(), "projects", config["project"], "test_reports", "screenshots")
                if not os.path.exists(screen_folder_path):
                    os.mkdir(screen_folder_path)
                if config["report"]["app_test"]:
                    driver = AppiumHelper.get_current_driver()
                elif not config["report"]["win_test"]:
                    driver = SeleniumHelper.get_current_driver()
                screenshot_file_path = os.path.join(screen_folder_path, "%s.png" % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))
                if config["report"]["win_test"]:
                    from utils.win32_helper import Win32Helper
                    Win32Helper.capture_screen(screenshot_file_path)
                else:
                    driver.save_screenshot(screenshot_file_path)
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screenshot_file_path
                extra = getattr(rep, 'extra', [])
                extra.append(item.config.pluginmanager.getplugin('html').extras.html(html))
                rep.extra = extra
        elif rep.skipped:
            total_sum += 1
            skip_sum += 1
            module_case[test_file][test_method] = "skip"
    print("Run %d cases, Current Status: Pass - %d, Fail - %d, Skip - %d" % (total_sum, pass_sum, fail_sum, skip_sum))
    current_result = {"Total": total_sum, "Pass": pass_sum, "Fail": fail_sum, "Skip": skip_sum, "End_Time": datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S.%f"), "Details": module_case}
    with open(stat_file, "w") as f:
        json.dump(current_result, f)


# update environment data in pytest-html report
def pytest_configure(config):
    if hasattr(config, '_metadata'):
        run_config_data = LoadConfig.load_config()
        if "Python" in config._metadata.keys():
            del config._metadata["Python"]
        if "Packages" in config._metadata.keys():
            del config._metadata["Packages"]
        if "Plugins" in config._metadata.keys():
            del config._metadata["Plugins"]
        if "JAVA_HOME" in config._metadata.keys():
            del config._metadata["JAVA_HOME"]
        config._metadata["Project"] = run_config_data["project"]
        config._metadata["Environment"] = run_config_data["environment"]
        if run_config_data["report"]["ui_test"]:
            if run_config_data["report"]["app_test"]:
                config._metadata["Mobile"] = run_config_data["mobile"]
                config._metadata["Device"] = run_config_data["device"]
            elif run_config_data["report"]["win_test"]:
                config._metadata["Type"] = "Windows Software"
            else:
                config._metadata["Browser"] = run_config_data["browser"]
        else:
            config._metadata["Type"] = "API"


# update the result table in pytest-html report
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    try:
        cells.insert(2, html.th('Description'))
        cells.insert(3, html.th('Time', class_='sortable time', col='time'))
        cells.pop()
    except:
        print("error occur, cannot update report")

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    try:
        cells.insert(2, html.td(report.description))
        cells.insert(3, html.td(datetime.datetime.utcnow(), class_='col-time'))
        cells.pop()
    except:
        print("error occur, cannot update report")
