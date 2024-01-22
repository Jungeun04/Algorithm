
N = int(input())
searchSpace = list(map(int,input().split()))
M = int(input())
queryItems = list(map(int,input().split()))

searchSpace.sort() # 이분 탐색을 위해 배열을 먼저 정렬

def binary_search(searchSpace, target):
      
    start, end = 0, len(searchSpace) - 1

    while start <= end:
        mid = (start + end) // 2
        if searchSpace[mid] == target:
            return 1
        elif searchSpace[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return 0

for queryItem in queryItems:
    result = binary_search(searchSpace, queryItem)
    print(result)
