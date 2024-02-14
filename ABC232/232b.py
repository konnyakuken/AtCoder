S = input()
T = input()
print(ord(S[0]),ord(T[0]))
ans = ord(S[0])-ord(T[0])
#xyz
#yza
for i in range(len(S)):
    print(ans)
    print((ord(S[i])-ans))
    print(chr((ord(S[i])-ans)))
    if(chr(ord(S[i])-ans)!=T[i]):
        print("No")
        exit()

print("Yes")