import sys
sys.getrecursionlimit()

N,M =map(int,input().split())
#road = [list(map(int,input().split())) for i in range(M)]
road =[[0]* N]

for i in range(M):
    A,B = map(int,input().split())




def dfs(x,y):
    if not(0 <= x < m) or not(0 <= y < n) or road[x][y] == "#": # 壁に当たったり、探索範囲外になった場合はreturn
        return
    if road[x][y] == "g": # ゴールを見つけたら”Yes”を出力して終了
        print("Yes")
        sys.exit()
        
    road[x][y] = "#" #探索済みを示すためのマーキング
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)


ans = []
while True:
    for i in range(N):
        start = i + 1
        for j in range(N):
            end = j + 1
            if(start == end):
                ans.append([start,end])
            
    break



print(road)