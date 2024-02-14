N = int(input())
C= list(map(int,input().split()))

if(N == 2):
    all = C[0]*C[1]
    all -= min(C)
else:
    max_num = max(C)
    max_place =C.index(max_num)
    C.pop(max_place)
    second_num = max(C)
    all = max_num * second_num - second_num

print(all%(1000000007))
