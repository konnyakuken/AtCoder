S=input()
ans=0
count=0
flag=False
for j in range(10):#oが5つ以上あるかの判定
        if(S[j]=="o"):
            count+=1

if(count>4):
    print(ans)
    exit()
count=0

for i in range(10000):
    num=str(i)#文字列を作成
    while(len(num)!=4):
        num="0"+num
    
    o_count=0
    for j in range(10):
        if(S[j]=="x"):
            
            if(str(j) in num):#×が含まれているとき
                flag=True
                break
        if(S[j]=="o"):
            if(str(j) not in  num):#〇が含まれていないとき
                flag=True
                break
        
    if(flag==False):
        count+=1    
    else:
        flag=False

print(count)

