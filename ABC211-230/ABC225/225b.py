N = int(input())
ans = list(map(int,input().split()))
for i in range(N-2):
    a,b = map(int,input().split())
    if(a in ans and b in ans):
       pass
    elif(a in ans):
        ans = [a]
    elif(b in ans):
        ans = [b]
    else:
        print("No")
        exit()

print("Yes")
