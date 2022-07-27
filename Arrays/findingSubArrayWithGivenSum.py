#Find subarray with given sum

def findSubArray(arr,n,sum):

    currentSum = arr[0]
    start =0

    i=1
    mainlist=[]

    while i<=n:

        while currentSum > sum and start < i-1:
            currentSum = currentSum - arr[start]
            start = start+1

        if currentSum == sum:
            mainlist.append(start+1)
            mainlist.append(i)
            return mainlist

        if i<n:
            currentSum = currentSum +arr[i]

        i=i+1
    return [-1]


noOfElements = int(input())
list1 =[]
for i in range(noOfElements):
    list1.append(int(input()))

sum1 = int(input())
result = findSubArray(list1,noOfElements,sum1)
for i in result:
    print(i,end=' ')
            