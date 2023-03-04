def sumN(n):
    if n==0:
        return 0
    smallout = sumN(n-1)
    output = smallout + n
    return output

a = sumN(int(input()))
print(a)