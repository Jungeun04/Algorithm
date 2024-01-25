[미로 탐색](https://www.acmicpc.net/problem/2178)

```python
from collections import deque

# 입력 받기
n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]

# 방문 배열 초기화 및 시작점 설정
visited = [[False] * m for _ in range(n)]
queue = deque([(0, 0)])
visited[0][0] = True
distance = [[1] * m for _ in range(n)]  # 이동 거리 저장

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 실행
while queue:
    x, y = queue.popleft()
    
    # 목표 도달 시
    if x == n - 1 and y == m - 1:
        print(distance[x][y])
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        # 미로 범위 내에서 이동할 수 있는 칸이며 아직 방문하지 않은 경우
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
            queue.append((nx, ny))
            visited[nx][ny] = True
            distance[nx][ny] = distance[x][y] + 1
```