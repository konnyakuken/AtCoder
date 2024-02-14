N = int(input())
n = N
ans = 0

AB = list()
minite = list()
floatTime = 0
backTime = 0
ATime = 0
BTime = 0

last = list()

for i in range(N):
    a,b = map(int,input().split())
    AB.append([a,b])
    minite.append(a/b)
time = sum(minite)/2


for a,b in AB:
    if(time >= a/b):
        ans += a
        time -= a/b
    else:
        ans += time * b
        print(ans)
        exit()

# while True:
#     ATime = minite[0]
#     if(floatTime+ATime >= backTime+BTime):
#         if(floatTime+ATime >= time):
#             last = [minite.pop(0),A]

        
#     else:
#         floatTime += minite.pop(0)
#         ans += A.pop(0)
#         n-=1
#     BTime = minite[-1]
#     if(backTime+BTime >= time):
#         pass
#     else:
#         backTime +=minite.pop(-1)
#         A.remove(-1)
#         n-=1

    

    


# # A, ASpeed = AB.pop(0)  
# # print(A, ASpeed)


# # for i in range(N):
# #     A,ASpeed = AB.pop(0)
# #     B,BSpeed = AB.pop(-1)
# #     Amin = A/ASpeed
# #     Bmin = B/BSpeed
# #     if(N == 3):
# #         pass
# #     else:



    
