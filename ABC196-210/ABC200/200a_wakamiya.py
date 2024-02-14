from sys import stdin

#N = int(stdin.readline())
N=int(input())
if(N%100==0):
    print(N//100)
else:
    print(N//100+1)