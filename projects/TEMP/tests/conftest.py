from configuration.config import LoadConfig
from py.xml import html
import pytest
import os
import datetime
import json


total_sum = pass_sum = fail_sum = skip_sum = 0
module_case = {}


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
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
        print("\nCase Duration: %ss ...%s" % (str(round(rep.duration, 2)), rep.outcome))
        print(rep.keywords)
        print(rep.location)
        print(rep.nodeid)
        print(rep.fspath)
        test_method = rep.nodeid.split("::")[-1]
        if rep.passed:
            if test_method not in module_case[test_file]:
                total_sum += 1
                pass_sum += 1
            module_case[test_file][test_method] = "pass"
        elif rep.failed:
            if test_method not in module_case[test_file]:
                total_sum += 1
                fail_sum += 1
            module_case[test_file][test_method] = "fail"
        elif rep.skipped:
            total_sum += 1
            skip_sum += 1
            module_case[test_file][test_method] = "skip"
        print("Run %d cases, Current Status: Pass - %d, Fail - %d, Skip - %d\n" % (total_sum, pass_sum, fail_sum, skip_sum))
        current_result = {"Total": total_sum, "Pass": pass_sum, "Fail": fail_sum, "Skip": skip_sum, "End_Time": datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S.%f"), "Details": module_case}
        with open(stat_file, "w") as f:
            json.dump(current_result, f)


# update environment data in pytest-html report
def pytest_configure(config):
    if hasattr(config, '_metadata'):
        run_config_data = LoadConfig.load_config()
        del config._metadata["Python"]
        del config._metadata["Packages"]
        del config._metadata["Plugins"]
        del config._metadata["JAVA_HOME"]
        config._metadata["Project"] = run_config_data["project"]
        config._metadata["Environment"] = run_config_data["environment"]
        if run_config_data["report"]["ui_test"]:
            if run_config_data["report"]["app_test"]:
                config._metadata["Mobile"] = run_config_data["mobile"]
            elif run_config_data["report"]["win_test"]:
                config._metadata["Type"] = "Windows Software"
            else:
                config._metadata["Browser"] = run_config_data["browser"]
        else:
            config._metadata["Type"] = "API"


# # update the summary data in pytest-html report
# @pytest.mark.optionalhook
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([html.p("location: in prefix")])
#     del(summary[1])
#     postfix.extend([html.p("location: in postfix")])


# update the result table in pytest-html report
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(datetime.datetime.utcnow(), class_='col-time'))
    cells.pop()

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)