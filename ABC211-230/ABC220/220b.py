K = int(input())
A,B = input().split()
a = 0
b = 0

for i in range(len(A)):
    a += int(A[-(i+1)])*(K**i)

for j in range(len(B)):
    b += int(B[-(j+1)])*(K**j)

print(a*b)
