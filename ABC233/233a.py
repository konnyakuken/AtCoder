X,Y = map(int,input().split())
if(Y>X):
    if((Y-X)%10 == 0):
        print((Y-X)//10)
    else:
        print((Y-X)//10+1)
else:
    print(0)
