# Radixsort Algorithim
def countSort(arr,pos):
    size=len(arr)
    output =[0]*size
    count=[0]*10

    for i in range(0,size):
        index = arr[i]//pos
        count[index%10]+=1


    for j in range(1,10):
        count[j]+=count[j-1]


    k=size-1 
    while k>=0:
        index = arr[k]//pos
        output[count[index%10]-1]=arr[k]
        count[index%10]-=1
        k-=1

    for s in range(0,size):
        arr[s]=output[s]

    
def radixSort(array1):
    
    maxNum= max(array1)

    position =1

    while maxNum//position >0:
        countSort(array1,position)
        position*=10


list1=[432,8,530,88,281,11,45,677,199]
print('Before Sorted',list1)

radixSort(list1)

print('After Sort',list1)

    


