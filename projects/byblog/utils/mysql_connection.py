from utils.mysql_helper import MysqlHelper
from configuration.config import LoadConfig


class MysqlConnection:

    def __init__(self):
        all_config = LoadConfig.load_config()
        current_env = all_config["environment"]
        self.env_config = all_config["env"][current_env]

    def connect(self, name):
        return MysqlHelper(self.env_config[name])
