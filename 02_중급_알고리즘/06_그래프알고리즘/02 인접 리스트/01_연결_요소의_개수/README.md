[연결 요소의 개수](https://wikidocs.net/206355)

연결 요소의 개수를 구하는 문제는 그래프 탐색 알고리즘을 사용하여 해결할 수 있습니다. 이 문제를 해결하기 위해 깊이 우선 탐색(DFS) 또는 너비 우선 탐색(BFS) 중 하나를 선택하여 사용할 수 있습니다. 여기서는 DFS를 사용하는 방법을 설명하겠습니다.

### 알고리즘 설계

1. **그래프 구성**: 주어진 간선 정보를 바탕으로 그래프를 구성합니다. 이 때, 그래프는 인접 리스트나 인접 행렬로 표현할 수 있습니다.
2. **DFS 함수 정의**: DFS를 수행하여 각 정점을 방문하고, 방문한 정점을 표시하는 함수를 정의합니다.
3. **연결 요소 탐색**: 모든 정점에 대해 아직 방문하지 않았다면, DFS를 시작하여 해당 정점과 연결된 모든 정점을 방문합니다. 이 과정에서 DFS를 시작하는 횟수가 곧 연결 요소의 개수가 됩니다.
4. **결과 출력**: 연결 요소의 개수를 출력합니다.

### 코드 구현

```python
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
```

이 코드는 주어진 그래프에서 연결 요소의 개수를 구하고 출력합니다. DFS를 사용하여 그래프를 탐색하며, 새로운 연결 요소를 발견할 때마다 카운트를 증가시킵니다. 모든 정점에 대해 DFS를 수행한 후, 카운트된 연결 요소의 개수가 곧 답이 됩니다.

---

BFS를 사용하면 재귀 호출에 의한 스택 오버플로우 문제를 방지할 수 있으며, 큰 그래프에서도 안정적으로 탐색을 수행할 수 있습니다.

### BFS를 사용한 연결 요소 개수 구하기

BFS를 이용하여 연결 요소를 탐색할 때는 다음과 같은 절차를 따릅니다:

1. 모든 정점에 대해 방문하지 않았다면, 해당 정점부터 BFS를 시작합니다.
2. BFS 동안 현재 정점과 연결된 모든 인접 정점을 방문하고, 방문하지 않은 정점이 있다면 큐에 추가합니다.
3. 큐가 빌 때까지 이 과정을 반복하여, 한 번의 BFS 수행으로 연결된 모든 정점을 방문합니다.
4. 이때 BFS를 시작하는 횟수가 곧 연결 요소의 개수가 됩니다.

### 코드 구현

```python
from collections import deque

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

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

# 연결 요소의 개수를 세는 변수
count = 0

# 모든 정점에 대해 BFS 수행
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        count += 1  # 새로운 연결 요소 발견

# 연결 요소의 개수 출력
print(count)
```

이 코드는 BFS를 사용하여 그래프의 모든 정점을 탐색하며, 탐색 시작 횟수를 통해 연결 요소의 개수를 계산합니다. 각 정점에 대해 방문하지 않았다면, 그 정점부터 BFS 탐색을 시작하고, 이 과정에서 방문하는 모든 정점을 현재 연결 요소의 일부로 처리합니다. 모든 정점에 대해 이 작업을 수행한 후, 연결 요소의 개수를 출력합니다.