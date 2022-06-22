def search(arr,key):
    for i in range(0,len(arr)):
        if arr[i]==key:
            return i


l=[2,3,5,688,13,56,345,7,87,4]
result=search(l,5)
print(result)


#Another method for linear search

def linearSearch(arr,key,currentindex):
    if currentindex == -1:
        return -1

    if arr[currentindex]==key:
        return currentindex

    return linearSearch(arr,key,currentindex-1)


list2=[8,45,23,13,76,54,23,89,564,122]
currentindex=len(list2)-1
result2=linearSearch(list2,76,currentindex)
print(result2)