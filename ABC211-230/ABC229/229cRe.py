N,W = map(int,input().split())
cheeseArray = list()
ans = 0
grams = 0
for i in range(N):
    A,B = map(int,input().split())
    cheeseArray.append([A,B])
    grams += B

cheeseArray.sort(reverse=True, key=lambda x:x[0])

for i in range(len(cheeseArray)):
    gram = min(cheeseArray[i][1],W)
    ans += gram*cheeseArray[i][0]
    W -= gram
print(ans)


