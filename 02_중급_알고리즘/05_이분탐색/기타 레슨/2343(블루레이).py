def min_bluray_size(lectures, M):
    # 최소값 설정: 가장 긴 강의의 길이
    start = max(lectures)
    # 최대값 설정: 모든 강의 길이의 합
    end = sum(lectures)
    
    # 이진 탐색 실행
    while start <= end:
        mid = (start + end) // 2    # 중간값 설정
        total = 0                   # 현재 블루레이에 녹화된 강의 길이의 합
        count = 1                   # 사용된 블루레이의 수
        
        # 각 강의를 순회하며 블루레이 분배
        for lecture in lectures:
            
            # 현재 블루레이에 강의를 추가할 수 있는 경우
            if total + lecture <= mid:
                total += lecture
            else:
                # 새 블루레이 사용
                count += 1
                total = lecture
        
        # 블루레이 개수가 M보다 많은 경우, 블루레이 크기 증가
        if count > M:
            start = mid + 1
        else:
            end = mid - 1
    
    return start

# 예제 입력
lectures = [1,2,3,4,5,6,7,8,9]  # 각 강의의 길이
M = 3                           # 블루레이 개수

# 최소 블루레이 크기 계산
result = min_bluray_size(lectures, M)

print(result)