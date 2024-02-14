pin = input()
sameCount = 0
stepsCount = 0

X = list()
for i in range(len(pin)):
    X.append(int(pin[i]))

for i in range(len(X) - 1):
    if(X[i]==X[i+1]):
        sameCount +=1
    if(X[i] == 9 and X[i+1] == 0):
        stepsCount +=1
    elif(X[i]+1 == X[i+1]):
        stepsCount +=1

if(stepsCount == 3 or sameCount == 3):
    print("Weak")
else:
    print("Strong")

