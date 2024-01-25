[단지번호붙이기](https://www.acmicpc.net/problem/2667)

이 문제를 해결하기 위한 접근 방법은 다음과 같습니다. 우선, 주어진 지도에서 연결된 집들의 모임, 즉 단지를 찾아내고, 각 단지별 집의 수를 계산해야 합니다. 이를 위해 깊이 우선 탐색(DFS) 또는 너비 우선 탐색(BFS) 알고리즘을 사용할 수 있습니다. 여기서는 DFS를 예로 들어 문제 해결 방법을 설명하겠습니다.

### 단계별 접근 방법

1. **입력 받기**: 지도의 크기 `N`과 지도 정보를 입력받습니다.
2. **DFS 함수 정의**: 현재 위치에서 상하좌우를 탐색하여 연결된 집들을 찾는 함수를 정의합니다.
3. **단지 찾기**: 모든 칸을 순회하며, 아직 방문하지 않은 집(`1`)을 발견할 때마다 DFS를 시작하여 단지를 찾습니다. 각 단지별 집의 수를 계산합니다.
4. **결과 출력**: 단지 수를 출력하고, 각 단지 내 집의 수를 오름차순으로 정렬하여 출력합니다.

### 코드 예시

아래는 위 단계를 구현한 파이썬 코드 예시입니다.

```python
N = int(input())  # 지도의 크기
map = [list(map(int, input())) for _ in range(N)]  # 지도 정보

visited = [[False] * N for _ in range(N)]  # 방문 여부 체크

# DFS 함수 정의
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N or map[x][y] == 0 or visited[x][y]:
        return 0
    visited[x][y] = True
    return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)

# 각 단지내 집의 수를 저장할 리스트
house_counts = []

# 모든 위치를 순회하며 단지 찾기
for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and not visited[i][j]:
            house_counts.append(dfs(i, j))

# 결과 출력
print(len(house_counts))  # 단지 수 출력
for count in sorted(house_counts):  # 오름차순으로 정렬하여 출력
    print(count)
```

이 코드는 입력된 지도에서 연결된 집들의 모임을 찾아, 단지별 집의 수를 계산하고 이를 오름차순으로 정렬하여 출력합니다. DFS를 사용하여 각 단지를 탐색하며, 방문하지 않은 집을 발견할 때마다 단지 내 집의 수를 계산합니다.
