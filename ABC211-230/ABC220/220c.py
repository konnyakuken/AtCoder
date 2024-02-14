N = int(input())
A = list(map(int,input().split()))
X = int(input())
A_all = sum(A)

ans = X//A_all
X = X - ans*A_all
A_add = 0
count = 0
for i in A:
    A_add += i
    count += 1
    if(X<A_add):
        print(count+ans*N)
        exit()