A,B = map(int,input().split())
A_bin = str(bin(A)).lstrip("0b")
B_bin = str(bin(B)).lstrip("0b")
ans = list()
A_len = len(A_bin)
B_len = len(B_bin)

for i in range(max(A_len,B_len)):
    if(i < min(A_len,B_len)):
        if(A_bin[-i]=="1"and B_bin[-i]=="1"):
            ans.append("0")
        elif(A_bin[-i]=="1" or B_bin[-i]=="1"):
            ans.append("1")
        else:
            ans.append("0")
    else:
        if(max(A_len,B_len)==A_len):
            ans.append(A_bin[-i])
        else:
            ans.append(B_bin[-i])
ans.reverse()
print(ans)
print(int("".join(ans),2))
        