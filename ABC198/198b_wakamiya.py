N=list(input())
count_back=0
count_front=0

if(len(N)==1):
    print("Yes")
    exit()

for i in reversed(N):#末尾のチェック
    if(i=='0'):
        count_back+=1
    else:
        break
    

for i in range(count_back):#先頭のチェック
    if(N[i]=='0'):
        count_front+=1
    else:
        break


if(count_back-count_front>0):
    for i in range(count_back-count_front):
        N.insert(0, "0")


leng=len(N)
parity=(len(N)%2)
if(parity==1):#奇数の時
    N.pop(int((leng-1)/2))#真ん中を取り除く
    leng-=1

num=0
for i in reversed(N):
    if(N[num]==i):
        pass
    else:
        print("No")
        exit()
    num+=1
    if(num==leng/2):
        print("Yes")
        exit()

 