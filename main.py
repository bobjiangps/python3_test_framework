from common.application import Application
from common.report.storage import Storage


if __name__ == "__main__":
    new_round = Application()
    new_round.run()
    Storage(new_round.start_time).run()
