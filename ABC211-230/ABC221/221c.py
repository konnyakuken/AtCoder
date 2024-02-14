N = list(input())
N.sort(reverse=True)
length = len(N)
a = list()
b = list()
if(length%2 == 0):
    for i in range(length//2):
        a.append(N.pop(0))
        b.append(N.pop(0))
else:
    for i in range((length-1)//2):
        a.append(N.pop(0))
        b.append(N.pop(0))
    a.append(N.pop(0))

for i in range(len(b)):
    if(a[i]!=b[i]):
        a[i],b[i]=b[i],a[i]
        break
print(int("".join(a))*int("".join(b)))
