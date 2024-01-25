
```python
N,M = map(int,input().split())

arr = input()
can = [True if thing=='H' else False for thing in arr]
telo = [False] * M
can = telo + can + telo
count = 0

for i in range(M,N+M):
    if arr[i-M] == 'P':
        for j in range(i-M,i+M+1):
            if can[j]:
                can[j] = False
                count += 1
                break
print(count)
```