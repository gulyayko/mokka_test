import os
from configparser import ConfigParser

config_file = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'environment/config.ini')))


class GetConfig:

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get(self, title, value):
        return self.config.get(title, value)
