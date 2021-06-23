import itertools
N=int(input())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

n=A.index(min(A))
m=B.index(min(B))

if n==m:#重複している可能性があるとき
    a=A[n]
    b=B[m]
    A.remove(a)
    B.remove(b)
    #被りを排除
    ans=min(a+b,max(min(A),b),max(a,min(B)))
    print(ans)
else:
    print(max(min(A),min(B)))


"""
C=min(list(itertools.product(A,B)))
print(C)
"""