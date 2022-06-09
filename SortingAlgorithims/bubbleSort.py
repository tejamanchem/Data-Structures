from array import array


def bubbleSort(arr):

    for i in range(len(arr)):
        
        for j in range(0,len(arr)-i-1):
            
            if arr[j] >arr[j+1]:
                
                temp = arr[j]

                arr[j] = arr[j+1]

                arr[j+1] = temp


noOfElements = int(input())
list1=[]
for ele in range(0,noOfElements):
    list1.append(int(input()))



bubbleSort(list1)

print(list1)
