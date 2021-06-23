V,T,S,D=map(int,input().split())
A=D/V
if A<=S and A>=T:
    print("No")
else:
    print("Yes")
