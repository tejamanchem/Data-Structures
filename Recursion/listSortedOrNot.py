def isSorted(a):

    l = len(a)

    if l==0 or l==1:
        return True

    if a[0]>a[1]:
        return False

    smallList = a[1:]
    smallerSortedList = isSorted(smallList)

    if smallerSortedList:
        return True
    else:
        return False


a = []
n= int(input())
for i in range(0,n):
    print('Enter number')
    a.append(int(input()))

print(isSorted(a))

