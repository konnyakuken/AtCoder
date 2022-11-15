N,K = input().split()
K = int(K)

def g1(arr):
    num = sorted()

def count_resort(arr):
    max_num = max(arr)
    min_num = min(arr)
    count = [0] * (max_num - min_num + 1)
    for ele in arr:
        count[ele - min_num] += 1
    #print(count)

    return [ele for ele, cnt in enumerate(count, start=min_num) for __ in range(cnt)]


for i in range(K):
    print(count_sort([1,4,3,7,12,0,235,45,33]))
    print(reversed(count_resort([1,4,3,7,12,0,235,45,33])))
