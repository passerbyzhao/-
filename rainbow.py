from random import choice
from time import sleep


FOREGROUND = list(range(30, 38))
BACKGROUND = list(range(40, 48))
MODE = list(range(0, 9))
RESET = '\033[0m'

def infinite_rainbow(word):
    while 1:
        foreclolor = str(choice(FOREGROUND))
        backcolor = str(choice(BACKGROUND))
        while foreclolor[-1] == backcolor[-1]:
            backcolor = str(choice(BACKGROUND))
        print('\r\033[1;' + foreclolor + ';' + backcolor + 'm' + str(word) + RESET, end='')
        sleep(0.1)

def rainbow(word):
    foreclolor = str(choice(FOREGROUND))
    backcolor = str(choice(BACKGROUND))
    while foreclolor[-1] == backcolor[-1]:
        backcolor = str(choice(BACKGROUND))
    print('\r\033[1;' + foreclolor + ';' + backcolor + 'm' + str(word) + RESET, end='')

if __name__ == '__main__':
    infinite_rainbow('RAINBOWrainbowRainbow')
