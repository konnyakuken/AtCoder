N = int(input())
price = 0

for i in range(N):
    price += i+1
    if(price >= N):
        print(i+1)
        exit()