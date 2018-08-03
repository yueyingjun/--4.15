#--------------------------------------------------------------------------------------------------
def Math(list,type = 0):         #函数回调求列表中的最小(最大)元素
    def fn(callback):
        if type == 0:
            print("Ⅰ.list1中的最小值:",callback(list,type))
        else:
            print("Ⅰ.list1中的最小值:",callback(list, type))
    return fn
list1 = [122,7,12,2,89,45,34]
@Math(list1,0)
def find(list,type):
    temp = list[0]
    for i in range(1, len(list)):
        if type == 0:                    #当type=0时，利用函数输出列表中最小元素的值
            if temp > list[i]:
                temp = list[i]
        elif temp < list[i]:             #否则，利用函数输出列表中最大元素的值
            temp = list[i]
    return temp
#-------------------------------------------------------------------------------------------------
def Min1(list):                  #for循环求列表中的最小元素
    min = list[0]
    for i in range(1,len(list)):
        if min > list[i]:
            min = list[i]
    return min
#-------------------------------------------------------------------------------------------------
def Min2(list):                  #while循环求列表中的最小元素
    temp = list[0]
    num = 1
    i = 0
    while num < len(list):
        if temp > list[i+1]:
            temp = list[i+1]
        num+=1
        i+=1
    return temp
#------------------------------------------------------------------------------------------------
def findmin(list):               #函数递归求列表中的最小元素
    min_value = list[0]
    if len(list) == 1:
        return min_value
    else:
        temp = findmin(list[1:])
        if temp < min_value:
            min_value = temp
    return min_value

list2 = [15,4,75,13,89,0]
list3 = [89,45,1,18,30,7]
list4 = [12,55,8,99,23,56]

print("Ⅱ.list2中的最小值:",Min1(list2))
print("Ⅲ.list3中的最小值:",Min1(list3))
print("Ⅳ.list4中的最小值:",findmin(list4))
#-------------------------------------------------------------------------------------------------


