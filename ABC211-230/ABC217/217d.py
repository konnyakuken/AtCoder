import bisect
import array
L,Q = map(int,input().split())
#i はint型　最初に0を入れる
l = array.array("i",[0,L])

for i in range(Q):
    c,x = map(int,input().split())
    if(c == 1):
        bisect.insort(l,x)
    else:
        binary_search = bisect.bisect(l,x)
        print(l[binary_search]-l[binary_search-1])
    
