N=input()
n=N
count=0
ans=0
num=len(N)

if N=="0":
    print(0)
    exit()
if N=="1":
    print(1)
    exit()

for i in range(len(N)):
    if N[i]=="1":
        count+=1
    else:
        break

number="1"
tes=N[1:]

if(count==0):

    for i in range(num):
        ans+=int(number)
        number+="1"
elif(int(tes)==0):#10,100,1000

    for i in range(num-1):
        ans+=int(number)
        number+="1"
    ans+=1
    print(ans)
    exit()
else:
    for i in range(num-1):#1,11,111
        ans+=int(number)
        number+="1"
    number="1"

    for i in range(num-count):#1,10,100…
        ans+=int(number)
        number=number+"0"

    if num!=count:
        for i in range(num):#1123→123→23

            if(N[0]=="1"):
                N=N[1:]
                ans+=int(N)+1
            else:
                break
    else:
        for i in range(num-1):#111→11→end

            if(N[0]=="1"):
                N=N[1:]
                ans+=int(N)+1
            else:
                break
        ans+=1


if (num-count)==1 and n[num-1]=="0":#110,1110
    ans-=1

print(ans)