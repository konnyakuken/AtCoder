S=list(input())
num=len(S)
S=S[::-1]
for i in range(num):
    if(S[i]=='6'):
        S[i]='9'
    elif(S[i]=='9'):
        S[i]='6'

print("".join(S))