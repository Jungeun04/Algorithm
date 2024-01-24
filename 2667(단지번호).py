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
