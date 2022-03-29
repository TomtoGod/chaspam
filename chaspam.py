from os import path
from sys import argv
from configparser import ConfigParser
from pyautogui import write
from time import sleep

FILEPATH = 'text.txt'


def get_filepath():
    if len(argv) < 2:
        return FILEPATH
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
    filepath = get_filepath()
    spam(filepath, default_config)
