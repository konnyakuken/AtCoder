N=(input())
n=len(N)
flont=[]
back=[]
num=0
if(n==1):#一桁
    print(0)
    exit()

for i in range(n):
    if(n/2>i):
        flont.append(N[i])
    else:
        back.append(N[i])
        

fmap=map(str,flont)
a=int("".join(fmap))
#print(a)
bmap=map(str,back)
b=int("".join(bmap))
#print(b)


if (n%2==1):#奇数
    for i in back:
        print("9",end="")
    exit()

if(a>b):#偶数
    print(a-1)
else:
    print(a)