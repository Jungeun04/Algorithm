[구간 합 구하기 5](https://www.acmicpc.net/problem/11660)

이 문제는 2차원 누적 합(prefix sum)을 사용하여 효율적으로 해결할 수 있습니다. 2차원 누적 합은 각 셀까지의 합을 저장하는 방식으로, 특정 구간의 합을 빠르게 계산할 수 있게 해줍니다.

### 알고리즘 설계

1. **2차원 누적 합 계산**: 주어진 2차원 배열에 대해 2차원 누적 합을 계산합니다.
2. **구간 합 계산**: 2차원 누적 합을 이용하여 주어진 구간 `(x1, y1)`부터 `(x2, y2)`까지의 합을 계산합니다.
3. **결과 출력**: 각 쿼리에 대한 결과를 출력합니다.

### 2차원 누적 합 계산 방법

2차원 누적 합 배열 `prefix_sum`을 다음과 같이 정의합니다:

- `prefix_sum[i][j]`: 원래 배열에서 `(1, 1)`부터 `(i, j)`까지의 부분 배열의 합

2차원 누적 합은 다음과 같이 계산할 수 있습니다:

```python
prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i][j]
```

여기서 `arr[i][j]`는 원래 배열의 `(i, j)` 위치에 있는 값입니다.

### 구간 합 계산 방법

구간 `(x1, y1)`부터 `(x2, y2)`까지의 합은 다음과 같이 계산할 수 있습니다:

```python
구간합 = prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1]
```

### 파이썬 코드 예시

```python
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
prefix_sum = [[0] * (N+1) for _ in range(N+1)]

# 2차원 누적 합 계산
for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i-1][j-1]

# 구간 합 계산 및 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1]
    print(result)
```

이 코드는 주어진 배열에 대해 2차원 누적 합을 계산하고, 각 쿼리에 대해 구간 합을 계산하여 출력합니다.