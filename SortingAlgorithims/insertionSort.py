# Insertion Sort Algorithim

def insertionSort(arr):

    for i in range(1,len(arr)):
        
        key = arr[i]

        j = i-1
        
        while j >=0 and key <arr[j]:

            arr[j+1] = arr[j]

            j =j-1

        arr[j+1] = key


list1=[9,5,1,4,2,3]

insertionSort(list1)

print(list1)