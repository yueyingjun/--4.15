# 寻找最小值问题
def ass(arr):
    t=arr[0]
    for i in range(1,len(arr)):
        if(t>arr[i]):
            t=arr[i]
    return t
aa=[13,11,6,9,18,1,5]
print(ass(aa))
