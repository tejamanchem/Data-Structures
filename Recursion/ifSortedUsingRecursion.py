def isSorted(a,size):

    if(size==0 or size==1):
        return True
    if(a[0]>a[1]):
        return False  
     
    slice1 = slice(1,len(a))
    isSmallSorted = isSorted(a[slice1],size-1)
    return isSmallSorted

a =[1,2,3,4,5,1]
if(isSorted(a,len(a))):
     print("YES")
else:
     print("NO")