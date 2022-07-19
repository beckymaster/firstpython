def factor(x): 
    print(x,"的因數有:") 
    for i in range(1, x + 1):
        if x % i == 0: 
            print(i, end=' ')

num = int(input('請輸入正整數:')) 
factor(num)
