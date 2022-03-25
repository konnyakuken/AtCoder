N=int(input())
count=0

for i in range(N+1):
    i=str(i)
    for j in range(len(i)):
        if i[j]=="1":
            count+=1
        else:
            break

print(count)