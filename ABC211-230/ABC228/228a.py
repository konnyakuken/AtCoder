S,T,X = map(int,input().split())
if(S<T and S<=X<T):
    print("Yes")
elif(S>T and ((S<=X) or (X<T)) == True):
    print("Yes")
else:
    print("No")
     
