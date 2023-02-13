S = list(input())
N = len(S)
if(len(S)!=8):
    print("No")
    exit()


if(S[0].isupper()== True and S[N-1].isupper()==True):
    S.pop(N-1)
    S.pop(0)
else:
    print("No")
    exit()
number = "".join(S)

if(number.isdigit() == True):
    number = int(number)
    if(100000 <= number < 999999):
        print("Yes")
    else:
        print("No")
else:
    print("No")



    
