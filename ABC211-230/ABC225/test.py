def judge():
    # 左上が1になりうるか確認
    for col in range(M):
        if B[0][col] % 7 == 0 and col != M - 1:
            return False

    # 左右に隣り合う要素の差が1か確認
    for row in range(N):
        for col in range(M - 1):
            if B[row][col] + 1 != B[row][col + 1]:
                return False

    # 上下に隣り合う要素の差が7か確認
    for row in range(N - 1):
        if B[row][0] + 7 != B[row + 1][0]:
            return False
    return True


N, M = map(int, input().split())
B = []
for _ in range(N):
    _b = list(map(int, input().split()))
    B.append(_b)

print("Yes" if judge() else "No")
