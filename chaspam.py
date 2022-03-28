import pyautogui
import time

FILEPATH = 'text.txt'

if __name__ == '__main__':
    time.sleep(5)
    text_file = open(FILEPATH, 'r')
    text_lines = text_file.readlines()
    for line in text_lines:
        pyautogui.write(line)
        time.sleep(0.5)
    text_file.close()
