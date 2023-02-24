def fact(n):
    print(n)
    if n == 0:
        return 1
    return n*fact(n-1)


n = fact(int(input()))
print(n)
