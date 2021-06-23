A,B=map(int,input().split())
a_sum=0
b_sum=0
for i in range(len(str(A))):
    a=A%10
    a_sum+=a
    A//=10
    #print(a_sum)
for i in range(len(str(B))):
    b=B%10
    B//=10
    b_sum+=b
    #print(b_sum)
if a_sum>=b_sum:
    print(a_sum)
else:
    print(b_sum)
