import os
import configparser
import argparse
import sys
from common.singleton import Singleton
from utils.yaml_helper import YamlHelper


class FileConfig:

    def __init__(self, file_path=None):
        self.file_config_path = file_path
    
    def get_running_parameter_from_file(self):
        if self.file_config_path:
            config_file = self.file_config_path
        else:
            config_file = os.path.join(os.getcwd(), "Running_Config.ini")
        cf = configparser.ConfigParser()
        cf.read(config_file)
        return dict(cf.items("Run Test"))

    
class CMDConfig:

    def __init__(self):
        self.command_args = None
    
    def set_command_parameter(self):
        parser = argparse.ArgumentParser()
        
        parser.add_argument("-p", "--project", metavar="Example", type=str, default="TEMP",
                            help="a string that indicates which project it will run with")
        parser.add_argument("-e", "--environment", metavar="QA", type=str, default="QA", choices=["INT", "QA", "Staging", "PROD"],
                            help="a string that indicates which environment to test (INT, QA, Staging, PROD)")
        parser.add_argument("-b", "--browser", metavar="Chrome", type=str, default="Chrome", choices=["IE", "Safari", "Chrome", "Firefox", "Edge", "MobileBrowser"],
                            help="a string that indicates which browser to run web test")
        parser.add_argument("-m", "--mobile", metavar="Android", type=str, default="Android", choices=["Android", "iOS"],
                            help="a string that indicates which mobile system to run mobile app test")
        parser.add_argument("-d", "--device", metavar="Device", type=str, default="iPhone",
                            help="a string that indicates which device to run mobile app test")
        # test_group = parser.add_mutually_exclusive_group()
        parser.add_argument("-t", "--test", metavar="test_class_name test_class_name.method_name", type=str, nargs="+",
                            help="a list of test classes or test methods which you want to run")
        parser.add_argument("-et", "--exclude_test", metavar="test_class_name test_class_name.method_name", type=str, nargs="+",
                            help="a list of test classes or test methods which not run")
        parser.add_argument("-pf", "--profile", metavar="tester", type=str, default="Bob",
                            help="a string about the peoples to receive test result by email")
        parser.add_argument("-T", "--tag", metavar="Happy_Path", type=str, default="All", choices=["All", "Happy_Path", "Bad_Path", "Sad_Path"],
                            help="a string about the tag to define which cases to run")
        parser.add_argument("-k", "--keyword", metavar="", type=str,
                            help="a string about the keyword to define which cases to run, match case name")
        parser.add_argument("-m", "--marker", metavar="", type=str,
                            help="a string about the marker to define which cases to run, like categorization")
        parser.add_argument("-ll", "--log_level", metavar="DEBUG", type=str, default="DEBUG", choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTEST"],
                            help="a string about log level to show log")
        
        self.command_args = parser.parse_args()
        return self.command_args.__dict__
    

class LoadConfig(Singleton):
    
    @classmethod
    def load_config(cls, name=None):
        args = sys.argv[1:]
        if len(args) < 1:
            all_config = FileConfig().get_running_parameter_from_file()
            all_config["config_type"] = "File"   
        elif len(args) == 1 and os.path.isfile(args[-1]):
            all_config = FileConfig().get_running_parameter_from_file(args[-1])
            all_config["config_type"] = "File"     
        else:
            all_config = CMDConfig().set_command_parameter()
            all_config["config_type"] = "Command"   
        public_conf = YamlHelper.load_yaml(os.path.join(os.getcwd(), "configuration", "public_config.yaml"))
        project_conf = YamlHelper.load_yaml(os.path.join(os.getcwd(), "projects", all_config["project"], "conf", "project_config.yaml"))
        project_conf["env"] = project_conf["env"][all_config["environment"]]
        all_config = dict(all_config, **public_conf)
        all_config = dict(all_config, **project_conf)
        if name:
            return all_config[name]
        else:
            return all_config


class TestData:

    @classmethod
    def load_test_case_data(cls, file_name):
        all_config = LoadConfig.load_config()
        test_data = []
        test_data_path = os.path.join(os.getcwd(), "projects", all_config["project"], "test_data", file_name + ".yaml")
        if os.path.exists(test_data_path):
            case_data = YamlHelper.load_yaml(test_data_path)
            for case in case_data.values():
                test_data.append(list(case.values()))
        return test_data

    @classmethod
    def load_test_case_data_by_section(cls, file_name, section_name):
        all_config = LoadConfig.load_config()
        test_data = []
        test_data_path = os.path.join(os.getcwd(), "projects", all_config["project"], "test_data", file_name + ".yaml")
        if os.path.exists(test_data_path):
            case_data = YamlHelper.load_yaml(test_data_path)
            if isinstance(case_data[section_name], list):
                test_data = case_data[section_name]
            elif isinstance(case_data[section_name], dict):
                test_data.append(case_data[section_name])
        return test_data
