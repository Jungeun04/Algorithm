from collections import deque

M, N = map(int, input().split())  # 상자의 가로, 세로 크기
box = [list(map(int, input().split())) for _ in range(N)]  # 토마토 상태

# 상하좌우 이동을 위한 방향 벡터 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 익은 토마토 위치를 찾아 큐에 저장
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j, 0))  # (x, y, 일수)

# BFS 실행
while queue:
    x, y, day = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            box[nx][ny] = 1  # 토마토를 익게 함
            queue.append((nx, ny, day + 1))

# 모든 토마토가 익었는지 확인하고 결과 출력
max_days = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:  # 익지 않은 토마토가 있다면
            print(-1)
            exit(0)
        max_days = max(max_days, day)

print(max_days)
