S = input()
num = len(S)
ans = False
T = ["o","x","x"]
if(num <= 2):
    if(S=="oo"):
        ans = False
    else:
        ans = True
else:
    circlePoint =  S.find("o")
    if(circlePoint == -1):
        ans = False
    else:
        flag = True
        for i in range(circlePoint,num):
            if(T[(i-circlePoint)%3]!=S[i]):
                flag = False
                break
        for i in reversed(range(circlePoint)):
            if(T[(i-circlePoint)%3]!=S[i]):
                flag = False
                break
        if(flag):
            ans = True
        else:
            ans = False

if(ans):
    print("Yes")
else:
    print("No")