H,W = map(int,input().split())
A = list()
for i in range(H):
    a = list(map(int,input().split()))
    A.append(a)

for i1 in range(H-1):
    for j1 in range(W-1):
        for i2 in range(i1+1,H):
            for j2 in range(j1+1,W):
                #print(i1,j1,i2,j2)
                if((A[i1][j1]+A[i2][j2])>(A[i2][j1]+A[i1][j2])):
                    print("No")
                    exit()
                
print("Yes")