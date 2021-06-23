A,B,W=map(int,input().split())
W*=1000

#dif=B-A
max=W//A
min=W//B
print(min,max)
if (max*A<=W and W<=min*B)==False:#min or max*A<=W<=min or max*Bなら解がある?
    print("UNSATISFIABLE")
else:
    print(min,max)
    #×