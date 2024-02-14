N = int(input())
ans = list()
while True:
    if(N % 2 == 0):
        N //=2
        ans.insert(0,"B")
    else:
        N -= 1
        ans.insert(0,"A")
    if(N <= 0):
        break

print("".join(ans))