abc=[12,3,56,2,88]
def aa(arr):
    for i in range(1,len(arr)):
        j=i-1
        if (arr[i]<arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            j-=1
            while (j>=0 and temp<arr[j]):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=temp
    return arr[0]
print("输出列表的最小数：",aa(abc))

