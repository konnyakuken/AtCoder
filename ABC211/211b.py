ans = ["H","2B","3B","HR"]
for i in range(4):
    S = input()
    if (S in ans) == True:
        ans.pop(ans.index(S))
    else:
        print("No")
        exit()
print("Yes")