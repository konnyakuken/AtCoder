x,y = map(int,input().split())
all = [0,1,2]
ans = 0
if(x == y):
    ans = x
else:
    ans = list(set(all)^set([x,y]))[0]

print(ans)
