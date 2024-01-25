[바이러스](https://www.acmicpc.net/problem/2606).

이 문제는 네트워크 상에서 연결된 컴퓨터들 사이의 연결 관계를 그래프로 모델링하고, 1번 컴퓨터에서 시작하여 연결된 모든 컴퓨터를 탐색하는 문제입니다. 이를 해결하기 위해서는 그래프 탐색 알고리즘인 깊이 우선 탐색(DFS) 또는 너비 우선 탐색(BFS)을 사용할 수 있습니다. 여기서는 BFS를 사용한 해결 방법을 제시하겠습니다.

### BFS(Breadth-First Search) 접근 방법

1. **그래프 구성**: 컴퓨터들 사이의 연결 관계를 그래프로 표현합니다. 그래프는 인접 리스트나 인접 행렬로 구현할 수 있습니다.
2. **BFS 실행**: 1번 컴퓨터에서 시작하여 네트워크 상에서 연결된 모든 컴퓨터를 탐색합니다.
3. **바이러스에 걸린 컴퓨터 수 계산**: 1번 컴퓨터로부터 탐색되어 바이러스에 걸린 컴퓨터의 수를 계산합니다.

### 파이썬 코드 예시

```python
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
```

이 코드는 1번 컴퓨터로부터 시작하여 네트워크 상에서 BFS를 수행하여 바이러스에 걸린 컴퓨터의 수를 계산하고 출력합니다. `graph`는 컴퓨터들 사이의 연결 관계를 나타내며, `bfs` 함수는 네트워크 상에서 연결된 컴퓨터를 탐색하여 바이러스에 걸린 컴퓨터의 수를 계산합니다.