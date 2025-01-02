def binarySearch(arr,target):
    return binarySearchInner(arr,target,0,len(arr)-1)
def binarySearchInner(arr,target,start:int,end:int):
    mid=int((start+end)/2)
    if start>end:
        return -1
    if target==arr[mid]:
        return mid
    elif target<arr[mid]:
        return binarySearchInner(arr,target,start,mid-1)
    else:
        return binarySearchInner(arr,target,mid+1,end)


if __name__=="__main__":
    arr=[1,2,4,6,8]
    print(binarySearch(arr,4))
