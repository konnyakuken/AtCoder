X = list(input())
X_dict = dict()
X_re_dict = dict()
for i in range(len(X)):
    X_dict[X[i]] = i
    X_re_dict[i] = X[i]
N = int(input())
S = list()

for i in range(N):
    name = input()
    name_num = list()
    for j in list(name):
        name_num.append(X_dict[j])
    S.append(name_num)
    
S=sorted(S)

for i in S:
    ans = ""
    for j in i:
        ans += X_re_dict[j]
    print(ans)






