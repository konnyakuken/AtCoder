"""L=int(input())
n=1
for i in range(11):
    n*=(i+1)
C=(L-1)*(L-2)*(L-3)*(L-4)*(L-5)*(L-6)*(L-7)*(L-8)*(L-9)*(L-10)*(L-11)/n
C+=0.00000000001
print(int(C))"""

L=int(input())
n=1
C=1
for i in range(11):
    C*=(L-(i+1))/(i+1)
C+=0.0000001
print(int(C))