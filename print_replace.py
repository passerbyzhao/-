from random import choice


FOREGROUND = [str(i) for i in range(30, 38)]    # 黑 红 绿 青 蓝 紫红 青蓝 白
BACKGROUND = [str(i) for i in range(40, 48)]    # 黑 红 绿 青 蓝 紫红 青蓝 白
MODE = [str(i) for i in range(0, 9)]    # 默认 高亮 下划线 闪烁 反白 不可见
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
    
