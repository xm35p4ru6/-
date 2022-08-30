import random

r = random.randint(1, 100)
while True:
    s = input('1~100, 請輸入一個數字: ')
    s = int(s)
    if s == r:
        print('恭喜你猜中了!!')
        break
    else:
        if s > r:
            print('在猜小一點')
        else:
            print('在猜大一點')