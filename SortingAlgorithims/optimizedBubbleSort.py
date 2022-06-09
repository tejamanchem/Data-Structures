def bubbleSort(arr):

    for i in range(len(arr)):

        swap = False

        for j in range(0,len(arr)-i-1):

            if arr[j] > arr[j+1]:

                temp = arr[j]
 
                arr[j]= arr[j+1]

                arr[j+1] = temp

            if not swap:
                break


noOfElements = int(input())

l1 =[]

for k in range(0,noOfElements):
    l1.append(int(input()))

bubbleSort(l1)

print(l1)



