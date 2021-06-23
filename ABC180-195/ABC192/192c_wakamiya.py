N,K=map(int,input().split())
x=[]
for i in range(K):
    while True:
        if 10>N:
            
            break
        x.append(N%=10)
        N/=10