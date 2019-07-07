from utils.mysql_helper import MysqlHelper
from configuration.config import LoadConfig


class MysqlConnection:

    def __init__(self):
        self.env_config = LoadConfig.load_config()["env"]

    def connect(self, name):
        return MysqlHelper(self.env_config[name])
