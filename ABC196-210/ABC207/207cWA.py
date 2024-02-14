N = int(input())
l = [0] * N
r = [0] * N
for i in range(N):
    typeNum,l[i],r[i] = map(int,input().split())
    #小数点を加味して2倍にする
    l[i]*=2
    r[i]*=2
    #type2に統一
    if(typeNum == 2):
        r[i]-=1
    elif(typeNum == 3):
        l[i]+=1
    elif(typeNum == 4):
        l[i]-=1
        r[i]+=1
count = 0
print(l)
print(r)

#ここ条件分岐が上手くいっていない
for i in range(N):
    for j in range(i,N):
        print(j)
        if(( r[i]<= l[j] or r[j]<=l[i])):
            count +=1
            print("i:",i,"j:",j)

print(count)


