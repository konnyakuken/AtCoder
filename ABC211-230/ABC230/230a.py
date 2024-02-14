N = int(input())

if (42 <= N):
    num = ((3-len(str(N)))*"0")+str(N+1)
    print("AGC"+num)
else:
    num = ((3-len(str(N))))*"0"+str(N)
    print("AGC"+num)