
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    print('this is largest for'+ str(arr) +'this is largest',largest)
    print('this is n',n)
    print('this is largest for'+ str(arr)+'this is l',l)
    print('this is largest for'+str(arr)+'this is r',r)
    if l < n and arr[i] < arr[l]:
        largest = l
        print('this is largest for'+str(arr)+'this is largest',largest)
    
    if r < n and arr[largest] < arr[r]:
        
        largest = r
        print('this is largest for'+str(arr)+'this is largest',largest)
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        print('this is arr[i] '+str(arr[i]) +'this is arr[largest]',str(arr[largest]))
        heapify(arr, n, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2)-1, -1, -1):
            print('this is i for '+ str(newNum) +' i in for loop ',i)
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
        
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)
    
arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))