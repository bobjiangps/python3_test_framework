import os
import configparser
import argparse
import sys
from common.singleton import Singleton
from utils.yaml_helper import YamlHelper


class FileConfig:
    
    def get_running_parameter_from_file(self, filepath=None):
        if filepath:
            config_file = filepath
        else:
            config_file = os.path.join(os.getcwd(),"Running_Config.ini")
        cf = configparser.ConfigParser()
        cf.read(config_file)
        return dict(cf.items("Run Test"))

    
class CMDConfig:
    
    def set_command_parameter(self):
        parser = argparse.ArgumentParser()
        
        parser.add_argument("-pr", "--project", metavar = "Example", type = str, default = "Example", choices=["TEMP","Android_BaiduMap","Example_Android","Example_API_Restful","Example_Web"], 
                    help = "a string that indicates which project it will run with (Example)")
        parser.add_argument("-e", "--environment", metavar = "QA", type = str, default = "QA", choices=["INT","QA","Staging","PROD"],
                    help = "a string that indicates which environment to test (INT, QA, Staging, PROD)")
        parser.add_argument("-b", "--browser", metavar = "Chrome", type = str, default = "Chrome", choices=["IE","Safari","Chrome","Firefox"],
                    help = "a string that indicates which browser to run web test")
        parser.add_argument("-m", "--mobile", metavar = "Android", type = str, default = "Android", choices=["Android","iOS"],
                    help = "a string that indicates which mobile system to run mobile app test")
        # test_group = parser.add_mutually_exclusive_group()
        parser.add_argument("-t", "--test", metavar = "test_class_name test_class_name.method_name", type = str, nargs = "+",
                    help = "a list of test classes or test methods which you want to run")
        parser.add_argument("-et", "--exclude_test", metavar = "test_class_name test_class_name.method_name", type = str, nargs = "+",
                    help = "a list of test classes or test methods which not run")
        parser.add_argument("-p", "--profile", metavar = "tester", type = str,default = "Bob",
                    help = "a string about the peoples to receive test result by email")
        parser.add_argument("-T", "--tag", metavar = "Happy_Path", type = str,default = "All", choices=["All","Happy_Path","Bad_Path","Sad_Path"],
                    help = "a string about the tag to define which cases to run")
        parser.add_argument("-ll", "--log_level", metavar = "DEBUG", type = str,default = "DEBUG", choices=["CRITICAL","ERROR","WARNING","INFO","DEBUG","NOTEST"],
                    help = "a string about log level to show log")
        
        self.command_args = parser.parse_args()
        return self.command_args.__dict__
    

class LoadConfig(Singleton):
    
    @classmethod
    def load_config(cls):
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
        all_config = dict(all_config, **public_conf)
        all_config = dict(all_config, **project_conf)
        return all_config