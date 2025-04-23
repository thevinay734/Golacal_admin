import configparser
import os

# Construct path to config.ini
config_path = os.path.join(os.path.dirname(__file__), "..", "configuration", "config.ini")
config = configparser.RawConfigParser()
config.read(config_path)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'baseUrl')

    @staticmethod
    def getUserEmail():
        return config.get('common info', 'username')

    @staticmethod
    def getUserPassword():
        return config.get('common info', 'password')
