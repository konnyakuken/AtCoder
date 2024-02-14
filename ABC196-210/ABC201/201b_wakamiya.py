N=int(input())
S=[]
T=[]
for i in range(N):
    s,t=input().split()
    S.append(s)
    T.append(int(t))

num=T.index(max(T))
T.pop(num)
S.pop(num)

num=T.index(max(T))

print(S[num])
