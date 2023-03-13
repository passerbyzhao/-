from random import choice


FOREGROUND = [str(i) for i in range(30, 38)]
BACKGROUND = [str(i) for i in range(40, 48)]
MODE = [str(i) for i in range(0, 9)]
RESET = '\033[0m'
printf = print


def print(word, background=False, *args, **kwargs):
    foreclolor = choice(FOREGROUND)
    backcolor = choice(BACKGROUND)
    while foreclolor[-1] == backcolor[-1]:
        backcolor = choice(BACKGROUND)
    if background:
        printf('\r\033[1;' + foreclolor + ';' + backcolor + 'm' + str(word) + RESET, *args, **kwargs)
    else:
        printf('\r\033[1;' + foreclolor + 'm' + str(word) + RESET, *args, **kwargs)


if __name__ == '__main__':
    print('RAINBOWrainbowRainbow')
    
