arr=[32,11,2,5,1]
def zuixiao(arr):
    for i in range(1,len(arr)):
      temp=arr[0]
      if temp>arr[i]:
            temp=arr[i]
    return temp   #返回temp，运行输出的才是最小值，返回arr的话，运行输出的是整个数组
print(zuixiao(arr))

arr=[32,5,1,5,8,2,16,2]
def quchong(arr):
    for i in arr:
        if arr.count(i)>1:
                del arr[arr.index(i)]
        i+=1
    return arr
print(quchong(arr))