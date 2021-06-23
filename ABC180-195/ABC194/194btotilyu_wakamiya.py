N=int(input())

for i in range(N):
    A,B=map(int,input().split())
    if i==0:
        A_min=A
        B_min=B
        flag=1
    if A_min>A and B_min>B:#共に最小
        tmp_A=A_min
        tmp_B=B_min
        A_min=A
        B_min=B
        flag=1
    elif A_min>A:
        A_min=A
        flag=0
    elif B_min>B:
        B_min=B
        flag=0

if flag==1:
    
elif A_min>=B_min:
    print(A_min)
else:
    print(B_min)