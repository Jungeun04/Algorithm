# https://www.acmicpc.net/problem/1654
# 랜선 자르기

# 이분탐색

K, N = map(int, input().split())

lines = [int(input()) for _ in range(K)]

start = 1
end = max(lines)


while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid

    if cnt < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)
