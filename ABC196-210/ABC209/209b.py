N,X = map(int,input().split())

count = 1
for A in input().split():
    A = int(A)
    if(count % 2 == 1):
        X -= A
    else:
        X -= A
        X += 1
    if(X < 0):
        print("No")
        exit()
    count += 1

print("Yes")

