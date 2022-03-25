import itertools

N,L=map(int,input().split())
count=3*N

all = itertools.permutations('012', L)
for x in all:
    print(x)
