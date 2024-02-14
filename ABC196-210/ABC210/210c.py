N,K = map(int,input().split())
c = list(map(int,input().split()))
all = list()
max_num = 0

for i in range(N):
    if(i<K):
        all.append(c[i])
        max_num = len(set(all))
    else:
        check = all.pop(0)
        if(check == c[i]):
            all.append(c[i])
        else:
            all.append(c[i])
            now =len(set(all))
            if(max_num <= now):
                max_num = now

    
print(max_num)

