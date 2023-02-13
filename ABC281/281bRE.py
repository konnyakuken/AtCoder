S = list(input())
N = len(S)

if(S[0].isupper()== True and S[N-1].isupper()==True):
    S.pop(N-1)
    S.pop(0)
else:
    print("No")
    exit()
count = N -3
number = 0
for i in range(count):
    if(S[i].isdigit() == True):
        number += int(S[i])*10**count
        count -= 1
    else:
        print("No")
        exit()

print(number)
if(len(str(number))==6 and 10*5<= number < 10**6):
    print("Yes")
else:
    print("No")


    
