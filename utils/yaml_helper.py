import yaml


class YamlHelper:

    @classmethod
    def load_yaml(cls, file_path):
        rf = open(file_path, "rb")
        ret = yaml.load(rf, Loader=yaml.SafeLoader)
        rf.close()
        return ret

    @classmethod
    def dump_yaml(cls, file_path, data):
        wf = open(file_path, "w")
        yaml.dump(data, wf)
        wf.close()
