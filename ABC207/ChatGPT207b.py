A,B,C,D = map(int,input().split())
# 容器に入っている水色のボールの個数
n = A
# 容器に入っている赤色のボールの個数
m = 0

# 必要な操作回数
count = 1

# 目標が達成されるまで繰り返し
while (n + B) / (m + C) > D:
  # 水色のボールを容器に追加
  n += B
  # 赤色のボールを容器に追加
  m += C
  # 操作回数をインクリメント
  count += 1
  if(count == 10**5):
    break

# 結果を出力
if (n + B) / (m + C) <= D:
  print(count)
else:
  print(-1)