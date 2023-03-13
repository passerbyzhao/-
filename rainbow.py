from random import choice
from time import sleep


FOREGROUND = [str(i) for i in range(30, 38)]
BACKGROUND = [str(i) for i in range(40, 48)]
MODE = [str(i) for i in range(0, 9)]
RESET = '\033[0m'


def infinite_rainbow(word, background=True):
    while 1:
        foreclolor = choice(FOREGROUND)
        backcolor = choice(BACKGROUND)
        while foreclolor[-1] == backcolor[-1]:
            backcolor = choice(BACKGROUND)
        if background:
            print('\r\033[1;' + foreclolor + ';' + backcolor + 'm' + str(word) + RESET, end='')
        else:
            print('\r\033[1;' + foreclolor + 'm' + str(word) + RESET, end='')
        sleep(0.1)


def rainbow(word, background=True):
    foreclolor = choice(FOREGROUND)
    backcolor = choice(BACKGROUND)
    while foreclolor[-1] == backcolor[-1]:
        backcolor = choice(BACKGROUND)
    if background:
        print('\r\033[1;' + foreclolor + ';' + backcolor + 'm' + str(word) + RESET)
    else:
        print('\r\033[1;' + foreclolor + 'm' + str(word) + RESET)
        

if __name__ == '__main__':
    infinite_rainbow('RAINBOWrainbowRainbow')
