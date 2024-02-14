# おまじない 再帰関数書くとき
import sys
sys.setrecursionlimit(1000000000)
#通常の再帰関数 O(n)

#繰り返し二乗法
def pow_n(x, n):
    if n == 0:
        return 1 
    else:
        return x * pow_n(x, n - 1)

#2^20 4^10 16^5 16*16^4 16*256^2
def pow_r(x,n):
    if n == 0:
        return 1
    if n % 2 == 0:
        print(x)
        return pow_r(x**2 , n//2)
    else:
        print(x)
        return x * pow_r(x**2,(n-1)//2)

A,B,C = map(int,input().split())
AC = pow_r(A,C)
BC = pow_r(B,C)

if(AC == BC):
    print("=")
elif(AC < BC):
    print("<")
else:
    print(">")