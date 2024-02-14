S = input()
T = input()
count = 0
char_list = list()
for i in range(len(S)):
    if(S[i]!=T[i]):
        count+=1
        char_list.append([S[i],T[i],i])

if(count == 1 or 2< count ):
    print("No")
elif(count == 0):
    print("Yes")
else:
    if(char_list[0][0]==char_list[1][1] and 
       char_list[0][1]==char_list[1][0] and 
       (char_list[1][2]-char_list[0][2])==1):
        print("Yes")
    else:
        print("No")