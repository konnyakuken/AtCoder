N=int(input())
a=list(map(int,input().split()))
b=list()
ans=0
len
#基準値Nの移動
for i in range(N):
    for j in range(i+1,N):
        for z in range(j+1,N):
           
            print(a[i],a[j],a[z])
            if not(a[i]==a[j] or a[j]==a[z] or a[i]==a[z]) and (i<j and j<z):
                 #条件をクリアした値をリストに入れる
                b.append(a[i]*100+a[j]*10+a[z])
                print("oooooooo{},{},{}".format(a[i],a[j],a[z]))
                #ans=ans+1
#すべて終わった後に重複分を削除する                
for n in range(len(b)):
    for m in range(n+1,len(b)):
        b.sort()
        if b[n]==b[m]:
            b.pop(m)
            print(b)
                
                
print(len(b))


 """コメントアウトすると上手くいかない？
                b.append(a[i]*100+a[j]*10+a[z])
                print("oooooooo{},{},{}".format(i+1,j+1,z+1))
                for n in range(len(b)):
                    if b[n]==a[i]*100+a[j]*10+a[z]:
                        #ans=ans-1
                        count=count+1
                if count>=2:#等しいのなら重複を削除
                        ans=ans-1                        
                count=0"""