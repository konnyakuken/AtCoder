N = int(input())
S = input()
for i in range(len(S)):
    if(i == (N-1)):
        if(S[i]=="o"):
            print("Yes")
        else:
            print("No")
