def binarysearch(arr,l,r,x):
    if r>=l:
        mid=(l+r)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,l,mid-1,x)
        else:
            return binarysearch(arr,mid+1,r,x)
    else:
        return-1
arr=[2,3,4,10,40]
print(arr)
x=int(input("enter the element to search:"))
result=binarysearch(arr,0,len(arr)-1,x)
if result!=-1:
    print("present at index%d"%result)
else:
    print("not present in array")
