N,K = map(int,input().split())
friends = []
distance = 0 

for i in range(N):
    A,B = map(int,input().split())
    friends.append([A,B])

friends = sorted(friends, reverse=False, key=lambda x: x[0])
count = len(friends)

while True:
     if(count != 1):
        if(friends[0][0] <= K):
            K+= friends.pop(0)[1]
            count -= 1
        else:
            break
     else:
        if(friends[0][0] <= K):
            K+= friends.pop(0)[1]
        break  

print(K)
