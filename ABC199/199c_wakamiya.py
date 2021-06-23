N=int(input())
S=list(input())
Q=int(input())
swap=False
for i in range(Q):
    T,A,B=map(int,input().split())
    if(T==2):
        if (swap):
            swap=False
        else:
            swap=True
    elif(T==1):
        if(swap):#反転時
            if(A<=N):
                a=S[(A+N)-1]
            elif(A>N):
                a=S[(A-N)-1]

            if(B<=N):
                b=S[(B+N)-1]
                S[(B+N)-1]=a
            elif(B>N):
                b=S[(B-N)-1]
                S[(B-N)-1]=a

            if(A<=N):
                S[(A+N)-1]=b
            elif(A>N):
                S[(A-N)-1]=b
        else:
            tmp=S[A-1]
            S[A-1]=S[B-1]
            S[B-1]=tmp

if(swap):
    print("".join(S[N:2*N])+"".join(S[0:N]))
else:
    print("".join(S))

"""
    S1=list()
    for i in range(N):
        S1.append(S.pop(0))
    print("".join(S)+"".join(S1))
37行目を上記のようにするとTLEが5問ほど出た。
"""



