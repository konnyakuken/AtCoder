import itertools

count =0
N = int(input())
A = list(map(int,input().split()))

for v in itertools.combinations(A, 2):
    if v[0] != v[1]:
        count += 1

print(count)
