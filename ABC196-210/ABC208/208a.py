A,B = map(int,input().split())

if(B < A):
    print("No")
    exit()

if(B <= A*6):
    print("Yes")
else:
    print("No")