N,K = map(int,input().split())
A = list(map(int, input().split()))
all = 0

A_reversed = sorted(A)

all= K // N 
K = K % N

#配りきれる時
if(K == 0):
    for i in A:
        print(all)
    exit()

border = A_reversed[0]
count = 0

#判定
for i in A_reversed:
    if (K == 0):
        break
    else:
        K -= 1
        count += 1

border = A_reversed[count -1]

#出力
for i in A:
    if(i <= border):
        print(all+1)
    else:
        print(all)

