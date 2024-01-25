[DNA 비밀번호](https://www.acmicpc.net/problem/12891)

이 문제는 슬라이딩 윈도우와 해시를 이용해 효율적으로 해결할 수 있습니다. 주어진 DNA 문자열 `S`에서 길이 `P`의 부분문자열 중 'A', 'C', 'G', 'T'가 각각 주어진 최소 개수 이상 등장하는 모든 경우의 수를 찾아야 합니다. 이를 위해 다음과 같은 단계로 접근할 수 있습니다:

1. **슬라이딩 윈도우 준비**: 길이 `P`의 윈도우를 DNA 문자열의 시작 부분에 위치시킵니다.
2. **문자 빈도수 계산**: 윈도우 내에 'A', 'C', 'G', 'T'의 등장 횟수를 계산합니다.
3. **조건 충족 여부 확인**: 각 문자의 등장 횟수가 주어진 최소 개수 조건을 만족하는지 확인합니다.
4. **윈도우 이동**: 윈도우를 한 칸씩 오른쪽으로 이동시키며 2~3단계를 반복합니다.
5. **비밀번호 후보 기록**: 조건을 만족하는 모든 부분문자열(비밀번호 후보)를 기록합니다.
6. **비밀번호 후보의 중복 제거**: 동일한 비밀번호 후보가 여러 번 등장할 수 있으므로, 중복을 제거합니다.
7. **결과 출력**: 조건을 만족하는 비밀번호의 종류 수를 출력합니다.

Python의 `collections.Counter`를 이용하여 각 문자의 빈도수를 쉽게 관리할 수 있습니다. 하지만, 입력 크기가 최대 1,000,000이므로, 모든 부분문자열을 직접 저장하고 중복 제거하는 방식은 메모리와 시간 측면에서 비효율적일 수 있습니다. 따라서, 조건을 만족하는 부분문자열의 개수만 세는 것으로 충분합니다.

아래는 위의 접근 방법을 간략하게 구현한 예시입니다. 이 예시는 최소 개수 조건을 만족하는 부분문자열의 개수를 세는 방법에 초점을 맞추고 있으며, 세부 구현은 문제의 요구사항에 따라 달라질 수 있습니다.

```python
from collections import Counter

# 입력 받기
S, P = map(int, input().split())
DNA = input().strip()
min_counts = list(map(int, input().split()))

# 부분문자열 조건 확인 함수
def check_condition(counter):
    if counter['A'] >= min_counts[0] and counter['C'] >= min_counts[1] and \
       counter['G'] >= min_counts[2] and counter['T'] >= min_counts[3]:
        return True
    return False

# 슬라이딩 윈도우 초기화
window = Counter(DNA[:P])
valid_substrings = 1 if check_condition(window) else 0

# 슬라이딩 윈도우 이동
for i in range(1, S - P + 1):
    window[DNA[i-1]] -= 1  # 윈도우에서 제거될 문자 빈도수 감소
    window[DNA[i+P-1]] += 1  # 윈도우에 추가될 문자 빈도수 증가
    
    if check_condition(window):
        valid_substrings += 1

print(valid_substrings)
```

이 코드는 각 문자의 최소 등장 횟수 조건을 만족하는 부분문자열의 개수를 세어 출력합니다. 조건을 만족하는지 확인하는 `check_condition` 함수는 `Counter` 객체를 인자로 받아, 각 문자의 등장 횟수가 주어진 최소 개수 이상인지 확인합니다.