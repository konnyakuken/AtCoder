N,M = map(int,input().split())

check = [0,1,2,3,4,5,6,7]
B = list(map(int,input().split()))
ans = False
for i in range(M-1):
    check.pop(-1)

if(B[0]%7 in check):
    for i in range(M) :
        if(B[i]%7== 0 and i != M-1):
            print("No")
            exit()      
    for i in range(M-1) :
        if((B[i]+1)!=B[i+1]):
            print("No")
            exit()
    for i in range(N-1):
        nextB = list(map(int,input().split()))
        for j in range(M):
            if((B[j]+7) != nextB[j]):
                print("No")
                exit() 
        B = nextB

else:
    print("No")
    exit()

print("Yes")

