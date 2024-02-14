S = input()
T = input()
differences = []

for s, t in zip(S, T):
    diff = (ord(t) - ord(s)) % 26
    differences.append(diff)
#print(differences)
if(len(set(differences))==1):
    print("Yes")
else:
    print("No")
