'''2、 猜数字游戏 计算出一个1~100之间的随机数由人来猜，计算机跟进人猜的数字进行对比，给出提示大一点，小一点，如果猜对了则结束游戏'''

import random


def Digit_Game():
    computer_num = random.randint(1, 100)
    while True:
        your_num = int(input('请输入1-100的整数！'))
        if your_num < computer_num:
            print("大一点！")
        elif your_num > computer_num:
            print("小一点！")
        else:
            print("恭喜你猜对了！")
            break


if __name__ == '__main__':
    Digit_Game()
