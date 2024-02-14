S1 = input()
S2 = input()
black_count = S1.count("#") + S2.count("#")
if(black_count == 2 and ((S1[0]==S2[1]=="#") or (S1[1]==S2[0]=="#"))):
    print("No")
else:
    print("Yes")