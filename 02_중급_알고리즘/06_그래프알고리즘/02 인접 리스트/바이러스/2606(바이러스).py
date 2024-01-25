from collections import deque

# 컴퓨터의 수와 연결된 컴퓨터 쌍의 수 입력 받기
n = int(input())
m = int(input())

# 그래프(네트워크) 초기화
graph = [[] for _ in range(n + 1)]

# 네트워크 상에서 직접 연결된 컴퓨터 쌍 정보 입력 받아 그래프 구성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    infected = 0
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                infected += 1
    return infected

# 1번 컴퓨터로부터 바이러스에 걸린 컴퓨터 수 출력
print(bfs(1))
