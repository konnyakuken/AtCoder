N = int(input())
A = list(map(int, input().split()))
sum = 0

for i in range(N):
    if(10 < A[i]):
        sum += (A[i] - 10)

print(sum)