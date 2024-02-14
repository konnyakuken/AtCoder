H,W,X,Y=map(int,input().split())
S=[]
for i in range(H):
    s=list(input())
    S.append(s)
count=0
X-=1
Y-=1

for i in range(W):#横の処理
    if(Y-i<0):
        break
    elif(S[X][Y-i]=="#"):
        break
    elif(S[X][Y-i]=="."):
        count+=1
    
for i in range(W):
    if(Y+i>=W):
        break
    elif(S[X][Y+i]=="#"):
        break
    elif(S[X][Y+i]=="."):
        count+=1
count-=1#重複を削除

for i in range(H):#タテの処理
    if(X-i<0):
        break
    elif(S[X-i][Y]=="#"):
        break
    elif(S[X-i][Y]=="."):
        count+=1

for i in range(H):
    if(X+i>=H):
        break
    elif(S[X+i][Y]=="#"):
        break
    elif(S[X+i][Y]=="."):
        count+=1
count-=2#重複を削除
print(count)
