def zuixiaozhi(arr,type=1):
    min=arr[0]
    for i in range(1,len(arr)):
        if type==1:
            if min>arr[i]:
                min=arr[i]
        else:
            if min<arr[i]:
                min=arr[i]
    return min
arr=[3,12,1,34]
print(zuixiaozhi(arr,2))
