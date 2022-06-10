#selection sort Algorithim

def selectionSort(arr,size):

    for i in range(size):

        min_value = i

        for j in range(i+1,size):

            if arr[j] < arr[min_value]:

                min_value= j

        arr[i],arr[min_value]= arr[min_value],arr[i]


list1= [9,-2,4,3,0,2,6,1]

lenghtoflist= len(list1)

selectionSort(list1,lenghtoflist)

print(list1)


        