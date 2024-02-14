N=int(input())
a=list(map(int,input().split()))
A=[]
print(a)
for i in range(N):#二進数に変換
    A.append(str(bin(a[i]))[2:])
print(A)
#len(A[i])で長さを調べて0を挿入
#隣接する値のMax、Minを調べて更新？