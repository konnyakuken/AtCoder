S = input()
ans = list()

for i in S:
    if i == "0":
        ans.append("1")
    else:
        ans.append("0")

print("".join(ans))