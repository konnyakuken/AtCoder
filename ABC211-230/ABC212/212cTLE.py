import itertools

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
min = 0
first = True
for v in itertools.product(A,B ):
    num = abs(v[0] - v[1])
    if(first == True):
        min = num
        first = False
    if(num<min):
        min = num

print(min)