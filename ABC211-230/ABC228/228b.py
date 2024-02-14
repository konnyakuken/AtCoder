N,X = map(int,input().split())
boolA = [False] * N
A = list(map(int,input().split()))

boolA[X-1] = True
X = A[X-1]
count = 1

while True:
    if(boolA[X-1]==False):
        boolA[X-1] = True
        X = A[X-1]
        count += 1
    else:
        print(count)
        break

