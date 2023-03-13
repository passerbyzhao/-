from random import choice
from time import sleep


FOREGROUND = [str(i) for i in range(30, 38)]    # 黑 红 绿 青 蓝 紫红 青蓝 白
BACKGROUND = [str(i) for i in range(40, 48)]    # 黑 红 绿 青 蓝 紫红 青蓝 白
MODE = [str(i) for i in range(0, 9)]    # 默认 高亮 下划线 闪烁 反白 不可见
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
