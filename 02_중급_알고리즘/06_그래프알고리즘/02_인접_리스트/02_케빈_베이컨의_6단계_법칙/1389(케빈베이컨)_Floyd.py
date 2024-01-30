INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신으로의 거리는 0으로 초기화
for i in range(1, N + 1):
    graph[i][i] = 0

# 친구 관계 입력 받아 초기화
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드-워셜 알고리즘 수행
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 케빈 베이컨 수 계산 및 최솟값 도출
min_value = INF
person = 0

for i in range(1, N + 1):
    sum_value = sum(graph[i][1:N+1])
    if sum_value < min_value:
        min_value = sum_value
        person = i

print(person)
