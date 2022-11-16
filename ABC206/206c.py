#全体を求めてそれから重複を消す
N = int(input())
A = list(map(int,input().split()))
com =  sorted(A)

all = N*(N-1)/2
duplication = 1

for i in  range(N):
    if i == N -1 :
        all -= duplication*(duplication-1)/2
        break
    elif com[i] == com[i + 1]:
        duplication += 1
    else:
        all -= duplication*(duplication-1)/2
        duplication = 1

print(int(all))

