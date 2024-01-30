import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())  # 정점의 개수 N, 간선의 개수 M

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력받아 그래프 구성
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부를 체크할 리스트 초기화
visited = [False] * (N + 1)

def dfs(start):
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            dfs(next)

# 연결 요소의 개수를 세는 변수
count = 0

# 모든 정점에 대해 DFS 수행
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1  # 새로운 연결 요소 발견

# 연결 요소의 개수 출력
print(count)
