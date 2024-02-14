A,B,C = map(int,input().split())
count = 1

while True:
    ans = C*count
    if(A <= ans and ans <= B):
        print(ans)
        exit()
    elif(B<ans):
        print(-1)
        exit()
    count+=1
