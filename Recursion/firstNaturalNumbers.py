def print1(n):
    if n==0:
        return
    print1(n-1)
    print('!!!!!!!!!!!!!!!!!!',n)


print1(int(input()))