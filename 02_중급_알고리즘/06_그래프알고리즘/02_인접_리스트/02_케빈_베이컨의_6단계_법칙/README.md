[케빈 베이컨의 6단계 법칙](https://www.acmicpc.net/problem/1389)

BFS는 시작 정점으로부터 도달 가능한 모든 정점까지의 최단 거리를 구할 수 있기 때문에, 모든 유저에 대해 BFS를 수행하여 각 유저의 케빈 베이컨 수를 계산할 수 있습니다. 각 유저를 시작점으로 하여 BFS를 실행하고, 다른 모든 유저까지의 거리(촌수)의 합을 구한 다음, 그 합이 가장 작은 유저를 찾으면 됩니다.

### BFS 접근 방법

1. **그래프 구성**: 유저 간의 친구 관계를 그래프로 구성합니다. 이 그래프는 양방향 그래프가 됩니다.
2. **BFS 실행**: 모든 유저에 대해 BFS를 수행하여, 해당 유저로부터 다른 모든 유저까지의 최단 거리를 계산합니다.
3. **케빈 베이컨 수 계산**: 각 유저의 케빈 베이컨 수(다른 모든 유저까지의 거리 합)를 계산합니다.
4. **결과 도출**: 가장 케빈 베이컨 수가 작은 유저를 찾습니다. 여러 명일 경우 번호가 가장 작은 유저를 출력합니다.

### 코드 구현

```python
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 친구 관계를 그래프로 구성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    distance = [-1] * (N + 1)
    distance[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for next in graph[current]:
            if distance[next] == -1:
                distance[next] = distance[current] + 1
                queue.append(next)
                
    return sum(distance)  # -1을 제외한 모든 거리의 합 반환

min_value = float('inf')
person = 0

# 모든 유저에 대해 BFS 실행 및 케빈 베이컨 수 계산
for i in range(1, N + 1):
    kevin_bacon_number = bfs(i)
    if kevin_bacon_number < min_value:
        min_value = kevin_bacon_number
        person = i

print(person)
```

이 코드는 각 유저에 대해 BFS를 실행하여, 해당 유저로부터 다른 모든 유저까지의 최단 거리의 합(케빈 베이컨 수)을 계산합니다. 계산된 케빈 베이컨 수 중 가장 작은 값을 가진 유저를 찾아 출력합니다. BFS를 사용함으로써 각 유저 간의 최단 경로를 효율적으로 찾을 수 있으며, 이를 통해 문제를 해결할 수 있습니다.
