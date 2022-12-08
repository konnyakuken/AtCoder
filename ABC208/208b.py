import math
P = int(input())

count = 0
result = list()

for i in range(10):
    result.append(int(math.factorial(i+1)))

while True:
    for num in reversed(result):
        if (P >= num):
            P -= num
            count += 1
            if(P == 0):
                print(count)
                exit()
            break

        
        

            
