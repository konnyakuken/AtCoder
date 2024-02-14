N = int(input())
A = list(map(int, input().split()))
A_sort = sorted(A)

for i in range(N):
    if(A_sort[i] != i+1):
        print("No")
        exit()
print("Yes")