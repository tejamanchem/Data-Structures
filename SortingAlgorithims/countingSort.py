# Count Sort Algorithm

def countSort(array):

    size = len(array)

    output = [0]*size

    count = [0]*10


    for i in range(0,size):
        count[array[i]] += 1


    for j in range(0,10):
        count[j]+=count[j-1]


    k= size-1

    while k>=0:
        output[count[array[k]]-1] = array[k]
        count[array[k] ]-=1
        k-=1

    for s in range(0,size):
        array[s]=output[s] 



data = [4,2,2,8,3,3,1]
print('Before sort',data)

countSort(data)

print('After Sort',data)