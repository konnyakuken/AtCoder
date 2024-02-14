S = input()
T = input()

if set(S) != set(T):
    print("No")
    exit()

index = []
for i in range(len(S)):
    print(S[i],T[i])
    if S[i] != T[i]:
        index.append(i)

if S == T or (len(index)==2 and abs(index[0]-index[1])==1):
    print("Yes")
else:
    print("No")