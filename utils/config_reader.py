import configparser
import os

class ConfigReader:
    _config_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "config",
        "config.ini"
    )

    _config = configparser.ConfigParser()

    @classmethod
    def read_config(cls):
        """Force reading the latest config file"""
        cls._config.read(cls._config_path)
        return cls._config.sections()  # Optional: debug

    @classmethod
    def get(cls, section, key):
        # Always read fresh before getting
        cls.read_config()
        if section not in cls._config:
            raise ValueError(f"Section '{section}' not found in {cls._config_path}")
        return cls._config.get(section, key)