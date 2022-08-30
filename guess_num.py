import random

r = random.randint(1, 100)
c = 0
while True:
    c += 1 # c = c + 1 (快寫法)
    s = input('1~100, 請輸入一個數字: ')
    s = int(s)
    print('猜第', c, '次')
    if s == r:
        print('恭喜你猜中了!!')
        break
    else:
        if s > r:
            print('在猜小一點')
        else:
            print('在猜大一點')