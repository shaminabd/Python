def b(n , k):
    if k > n :
        return 0
    elif n >=k and k == 0:
        return 1
    else:
        return b(n-1, k) + b(n-1, k-1)

n, k = map(int, input().split())
print(b(n, k))

