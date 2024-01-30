from collections import deque

n = int(input())  # 전체 사람의 수
person1, person2 = map(int, input().split())  # 촌수를 계산해야 하는 두 사람
m = int(input())  # 부모 자식들 간의 관계의 개수

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 부모 자식간의 관계 입력받아 그래프 구성
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# BFS를 위한 준비
visited = [False] * (n + 1)
distance = [0] * (n + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                distance[next] = distance[current] + 1
                queue.append(next)

# BFS 실행
bfs(person1)

# 결과 출력
if visited[person2]:
    print(distance[person2])
else:
    print(-1)
