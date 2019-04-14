from configuration.config import LoadConfig
from py.xml import html
import pytest
import os
import datetime


pass_sum = fail_sum = skip_sum = 0


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    stat_file = os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "test_reports", "stat.csv")
    global pass_sum
    global fail_sum
    global skip_sum
    outcome = yield
    rep = outcome.get_result()
    rep.description = str(item.function.__doc__)
    setattr(item, "rep_" + rep.when, rep)
    if rep.when == "call":
        print("\nCase Duration: %ss ...%s" % (str(round(rep.duration, 2)), rep.outcome))
        print(rep.keywords)
        print(rep.location)
        print(rep.nodeid)
        print(rep.fspath)
        if rep.passed:
            pass_sum += 1
        elif rep.failed:
            fail_sum += 1
        elif rep.skipped:
            skip_sum += 1
        print("Current Status: Pass - %d, Fail - %d, Skip - %d\n" % (pass_sum, fail_sum, skip_sum))
        with open(stat_file, "w") as f:
            f.write("Pass,%d\nFail,%d\nSkip,%d\nEndTime,%s" % (pass_sum, fail_sum, skip_sum, datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")))


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