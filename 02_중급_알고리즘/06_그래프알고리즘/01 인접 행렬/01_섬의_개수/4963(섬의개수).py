import sys
sys.setrecursionlimit(10 ** 4)

def dfs(x, y):
    # 현재 위치를 방문 처리
    visited[x][y] = True
    # 8가지 방향에 대해 확인
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        nx = x + dx
        ny = y + dy
        
        # 지도 범위 내에 있고, 방문하지 않은 땅이라면 DFS 수행
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    islands = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                islands += 1
    print(islands)
