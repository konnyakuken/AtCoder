import itertools
N=int(input())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

a_min=min(A)
b_min=min(B)

n=A.index(a_min)
m=B.index(b_min)

if n==m:#重複している可能性があるとき
    a=A[n]
    b=B[m]
    A.remove(a)
    B.remove(b)
    #被りを排除
    ans=min(a+b,max(min(A),b),max(a,min(B)))
    print(ans)
else:
    print(max(a_min,b_min))


"""
C=min(list(itertools.product(A,B)))
print(C)
"""