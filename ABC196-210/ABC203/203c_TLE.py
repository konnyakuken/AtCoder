N,K = map(int,input().split())
friends = []
distance = 0 

for i in range(N):
    A,B = map(int,input().split())
    friends.append([A,B])

friends = sorted(friends, reverse=False, key=lambda x: x[0])

flag = 0

count = len(friends)

while True:
    number = 0
    sum = 0
    while True:
        if(count == 1):
            number = friends[0][0]
            sum += friends[0][1]
            flag = 1
            break
        
        if(friends[0][0] == friends[1][0] ):
            number = friends[0][0]
            sum += friends.pop(0)[1]
            count -= 1
        else:
            number = friends[0][0]
            sum += friends.pop(0)[1]
            count -= 1
            break

    if(number <= K):
        K += sum

        if(flag == 1):
            distance = K
            break
    else:
        distance = K
        break

print(distance)
    
