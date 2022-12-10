def C(n,k):
    if k > n:
        return 0
    elif k==n and k == 0:
        return 1
    else:
        return C( n-1, k) + C( n-1, k-1 )
n=int(input())
k=int(input())
print(C(n,k))
