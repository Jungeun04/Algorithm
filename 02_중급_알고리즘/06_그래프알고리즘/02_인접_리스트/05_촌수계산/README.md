[촌수계산](https://www.acmicpc.net/problem/2644)

이 문제는 그래프 탐색 알고리즘을 사용하여 해결할 수 있습니다. 특히, 너비 우선 탐색(BFS)를 활용하면 주어진 두 사람의 촌수를 효율적으로 계산할 수 있습니다. BFS를 사용하면 시작 정점으로부터 각 정점까지의 최단 경로, 즉 이 경우에는 촌수를 찾을 수 있습니다.

### 문제 해결 접근 방법

1. **그래프 구성**: 사람들과 그들 사이의 부모-자식 관계를 그래프로 표현합니다. 이 때, 그래프는 양방향으로 연결되어야 합니다(부모 → 자식, 자식 → 부모), 왜냐하면 촌수 계산은 양방향으로 가능해야 하기 때문입니다.
2. **BFS 실행**: 주어진 두 사람 중 한 사람을 시작 정점으로 하여 BFS를 실행하고, 다른 한 사람에 도달할 때까지의 거리(촌수)를 계산합니다.
3. **촌수 계산**: BFS를 통해 탐색한 거리가 바로 두 사람 사이의 촌수입니다. 만약 BFS 탐색 중에 다른 한 사람에 도달하지 못했다면, 두 사람 사이에 촌수를 계산할 수 없는 것으로 -1을 출력합니다.

### 코드 구현

```python
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
```

이 코드는 주어진 두 사람 사이의 촌수를 BFS를 통해 계산하고, 그 결과를 출력합니다. BFS를 실행하여 한 사람으로부터 다른 사람까지의 최단 거리(촌수)를 찾으며, 만약 두 사람이 연결되어 있지 않다면 `-1`을 출력합니다.