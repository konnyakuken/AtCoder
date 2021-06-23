S=input()
check=2
flag=0
for i in S:
    if len(S)==1:
        if 65<=ord(i) and ord(i)<=90:
            print("No")
        else:
            print("Yes")
        flag=1
        break

    if check!=2:
        #ord()でアスキーコードを取得
        if 65<=ord(i) and ord(i)<=90:
            a=0#大文字
        else:
            a=1#小文字
        if a==check:
            flag=1
            print("No")
            break
  
    if 65<=ord(i) and ord(i)<=90:
        check=0
    else:
        check=1

if flag==0:
    print("Yes")
    