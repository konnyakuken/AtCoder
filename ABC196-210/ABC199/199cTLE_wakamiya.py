#TLEが出る
N=int(input())
S2=list(input())
S1=list()

for i in range(N):
    S1.append(S2.pop(0))
Q=int(input())
for i in range(Q):
    T,A,B=map(int,input().split())
    if(T==2):
        tmp=S1
        S1=S2
        S2=tmp
    elif(T==1):
        if(A<=N):
            tmpA=S1[A-1]
        elif(A>N):
            tmpA=S2[(A-N)-1]
        
        if(B<=N):
            tmpB=S1[B-1]
            S1[B-1]=tmpA
        elif(B>N):
            tmpB=S2[(B-N)-1]
            S2[(B-N)-1]=tmpA

        if(A<=N):
            S1[A-1]=tmpB
        elif(A>N):
            S2[(A-N)-1]=tmpB

print("".join(S1)+"".join(S2))
