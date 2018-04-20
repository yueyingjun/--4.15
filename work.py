#最小值
list=[5,3,9,7,1]
for i in range(len(list)):
    j=i-1
    while list[i]>list[j]:
        temp=list[j]
        list[j]=list[i]
        list[i]=temp
        j-=1
print(list[i])
#删除相同值
list1=[6,6,5,9,8,3,5,3,4,9,6]
def sortlist(list):
    list1.sort()
    last=list1[-1]
    for i in range(len(list1)-2,-1,-1):
        if list1[i]==last:
            list1.remove(list1[i])
        else:
            last=list1[i]
    return list
print(sortlist(list1))
