N = int(input())
C= list(map(int,input().split()))

if(N == 2):
    all = C[0]*C[1]
    all -= min(C)
else:
    max_num = max(C)
    max_place =C.index(max_num)

    flont_num = max(C[:max_place])
    back_num = max(C[(max_place+1):])
    if(flont_num == max_num or back_num == max_num):
        all = max_num*max_num -max_num
    else:
        all = flont_num * max_num - flont_num
        all += (max_num - flont_num) *back_num

print(all%(10**9+7))
