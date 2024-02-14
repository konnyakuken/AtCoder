N,K = map(int,input().split())
c = list(map(int,input().split()))

max_num = 0

for i in range(N):
    if((i+K)<= N):
        check = list(set(c[i:i+K]))
        result = len(check)
        if(result>max_num):
            max_num = result
    else:
        break
    
print(max_num)

