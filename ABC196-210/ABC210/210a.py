N,A,X,Y = map(int,input().split())

sale = N - A
if (sale >=0):
    print(A*X+sale*Y)
else:
    print(N*X)