X = int(input())
border = [0,40,70,90]
if(border[-1] <= X):
    print("expert")
    exit()

for i in reversed(range(1,len(border))):  
    if(border[i-1]<= X and X < border[i]):
        print(border[i]-X)
        exit()
