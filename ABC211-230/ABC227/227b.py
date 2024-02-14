N = int(input())
S = list(map(int,input().split()))
S.sort()
count = N

for a in range(1,1001):
    for b in range(1,1001):
        nowValue = 4*a*b + 3*a + 3*b
        for i in range(len(S)):
           if(nowValue == S[i]):
               count -=1
               #S.pop(i)
               S[i]= 0
               
print(count)
