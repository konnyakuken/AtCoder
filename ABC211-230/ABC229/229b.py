A_str,B_str = map(str,input().split())
A = list(A_str)
B = list(B_str)
A.reverse()
B.reverse()
for i in range(min(len(A),len(B))):
    if((int(A[i])+int(B[i]))>=10):
       print("Hard")
       exit()

print("Easy")