from configuration.config import LoadConfig
import pytest
import os
import datetime


pass_sum = fail_sum = skip_sum = 0


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    stat_file = os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "test_reports", "stat.csv")
    global pass_sum
    global fail_sum
    global skip_sum
    outcome = yield
    rep = outcome.get_result()
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
