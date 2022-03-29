from os import path
from sys import argv
from configparser import ConfigParser
from pyautogui import write
from time import sleep


def get_filepath(default_config):
    if len(argv) < 2:
        return default_config['default_text_file']
    return argv[1]


def load_config_file():
    config = ConfigParser()
    dir_path = path.dirname(path.realpath(__file__))
    config.read(dir_path + "/chaspam.ini")
    return config


def spam(filepath: str, default_config):
    text_file = open(filepath, 'r')
    text_lines = text_file.readlines()
    for line in text_lines:
        write(line)
        sleep(float(default_config['message_delay']))
    text_file.close()


if __name__ == '__main__':
    config = load_config_file()
    default_config = config['default']
    sleep(float(default_config['initial_delay']))
    filepath = get_filepath(default_config)
    spam(filepath, default_config)
