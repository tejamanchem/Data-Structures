
def insertionSort(arr1):

    for i in range(1,len(arr1)):
        up=arr1[i]
        j=i-1
        while j>=0 and arr1[j]>up:
            arr1[j+1]=arr1[j]
            j-=1
        arr1[j+1]=up

    return arr1

def bucketSort(arr):
    bucket=[]
    sort_num =10

    for i in range(sort_num):
        bucket.append([])

    for j in arr:
        index_b = int(sort_num * j)
        bucket[index_b].append(j)

    for k in range(sort_num):
        bucket[k]= insertionSort(bucket[k])

    s=0
    for l in range(sort_num):
        for h in range(len(bucket[l])):
            arr[s]=bucket[l][h]
            s+=1
    return arr


x = [0.897, 0.565, 0.656,
	0.1234, 0.665, 0.3434]
bucketSort(x)
print(x)