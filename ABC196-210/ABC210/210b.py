N = int(input())
S = input()
length = len(S)
count = 0
for i in range(length):
    if(S[i] == "1"):
        if(count%2 == 0):
            print("Takahashi")
        else:
            print("Aoki")
        exit()
    count+=1