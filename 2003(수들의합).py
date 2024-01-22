n, m = map(int, input().split())  # N과 M을 입력받음
a = list(map(int, input().split()))  # 수열 A를 입력받음

count = 0  # 조건을 만족하는 경우의 수
interval_sum = 0  # 현재 구간의 합
end = 0  # 끝 포인터

# 시작 포인터(start)를 이동시키면서 반복
for start in range(n):
    # 구간의 합이 M보다 작고, end가 수열의 끝에 도달하지 않았다면
    while interval_sum < m and end < n:
        interval_sum += a[end]  # 구간의 합에 a[end] 값을 더함
        end += 1                # 끝 포인터를 오른쪽으로 이동

    # 구간의 합이 M과 같다면 경우의 수를 증가
    if interval_sum == m:
        count += 1
    interval_sum -= a[start]  # 시작 포인터가 가리키는 값을 구간의 합에서 빼고 오른쪽으로 이동

print(count)  # 경우의 수 출력
