A, B, C = map(int, input().split())

a = A//C
b = B//C
print(a,b)
if(a==b):
    print(-1)
else:
    print(b*C)