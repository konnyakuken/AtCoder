a,b,c,d = map(int,input().split())
count = 1
if(b >= c*d):
    print(-1)
    exit()
while True:
    if((a+(b*count)) <= (c*count)*d):
        print(count)
        exit()
    count+=1
