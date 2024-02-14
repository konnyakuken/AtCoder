N = int(input())
S = list()
T = list()
S_sharp = [0]* N
T_sharp = [0]* N

for i in range(N):
    s = list(input())
    S.append(s)

for i in range(N):
    t = list(input())
    T_sharp[i]=t.count("#")
    T.append(t)

print(S)
print(T)

for i in range(4):
    S_left = list()
    num = 0
    isSame = True
    #回転＆シャープ確認
    for j in reversed(range(N)):
        s_l = list()
        for k in range(N):
            s_l.append(S[k][j])
        S_sharp[num] = ("".join(s_l)).count("#")
        num += 1
        S_left.append(s_l)
    S = S_left
    #並行移動で行けるかcheck
    for j in range(N):
        if(S_sharp[j]!=T_sharp[j]):
            isSame = False
            break
    # if(isSame == True):
    #     for j in range(N):
    #         for 
    print(S_sharp,T_sharp)
    print(isSame)

        


print("No")





