import yaml
# import os

# the following class is used for including another yaml file, like: "c: !include t.yaml"
# class Loader(yaml.Loader):
#
#     def __init__(self, stream):
#         self._root = os.path.split(stream.name)[0]
#
#         super().__init__(stream)
#
#     def include(self, node):
#         filename = os.path.join(self._root, self.construct_scalar(node))
#
#         with open(filename, 'r') as f:
#             return yaml.load(f, Loader)
#
#
# Loader.add_constructor('!include', Loader.include)


class YamlHelper:

    @classmethod
    def load_yaml(cls, file_path):
        with open(file_path, "r") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            # data = yaml.load(f, Loader=Loader) # the class above
        return data

    @classmethod
    def dump_yaml(cls, file_path, data):
        with open(file_path, "w") as f:
            yaml.dump(data, f)
