import random
s = input('請輸入開始值')
e = input('請輸入結束值')
s = int(s)
e = int(e)

r = random.randint(s, e)
c = 0
while True:
    c += 1 # c = c + 1 (快寫法)
    s = input('請輸入一個數字: ')
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