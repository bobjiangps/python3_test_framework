import yaml


class YamlHelper(object):

    @classmethod
    def load_yaml(self, f):
        rf = open(f, "rb")
        ret = yaml.load(rf)
        rf.close()
        return ret

    @classmethod
    def dump_yaml(self, f, dataMap):
        wf = open(f, "w")
        yaml.safe_dump(dataMap, wf)
        wf.close()
