A,B = map(int,input().split())
A_bin = str(bin(A)).lstrip("0b")
B_bin = str(bin(B)).lstrip("0b")
ans = list()
for i in range(min(len(A_bin),len(B_bin))):
    ans.append(int(A_bin[-i])^int(B_bin[-i]))

if(len(A_bin)!=len(B_bin)):
    for i in range(max(len(A_bin),len(B_bin))-min(len(A_bin),len(B_bin))):
        if(len(A_bin)>len(B_bin)):
            ans.append(A_bin[i])
        else:
            ans.append(B_bin[i])

print(ans)