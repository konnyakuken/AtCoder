S=input()
check=2
flag=0
for i in S:
    if len(S)==1:
        if i.islower():
            print("Yes")
        else:
            print("No")
        flag=1
        break
    
    if i.islower()==True and check==0 or i.islower()==False and check==1 :
        print("No")
        flag=1
        break

    if i.islower():
        check=0#小文字 
    else:
        check=1#大文字

if flag==0:
    print("Yes")
    