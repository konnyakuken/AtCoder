N,S,D=map(int,input().split())
flag=0
for i in range(N):
    X,Y=map(int,input().split())
    if X<S and Y>D:
        flag=1
if flag==1:
    print("Yes")
else:
    print("No")