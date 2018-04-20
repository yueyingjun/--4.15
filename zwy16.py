# 排除相同值问题
def ass(arr):
    for i in range(0,len(arr)):
        for j in range(i+2,len(arr)):
            j=j-1
            if(arr[i]==arr[j]):
                del arr[j]
    for i in range(0,len(arr)-2):
        if(arr[i]==arr[-1]):
            ass.pop()
    return arr
aa=[12,1,2,3,12,2,13,1,2,12]
print(ass(aa))



