def POW(a,b,m):
    if b == 1:
        return a%m
    else:
        temp = POW(a,b//2,m)

        if b % 2 == 0:
            return temp * temp % m
        else:
            return temp * temp * a % m

A,B,M = map(int,input().split())

print(POW(A,B,M))
