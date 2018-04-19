#-------------------------------------------------------------------------------
def clean1(list):                      #用for循环实现数据去重
    temp_list = []
    for num in list:
        if num not in temp_list:
            temp_list.append(num)
    return temp_list

list1 = [2,2,2,2,0,0,0,0,1,1,1,1,8,8,8,8]
print("去重后的列表1为:",clean1(list1))
#------------------------------------------------------------------------------
def clean2(list):                      #用while循环实现数据去重
    temp_list = []
    i = 0
    while i != len(list):
        num = list[i]
        if num not in temp_list:
            temp_list.append(num)
        i+=1
    return temp_list

list2 = [0,0,0,0,4,4,4,4,1,1,1,1,5,5,5,5]
print("去重后的列表2为:",clean2(list2))
#------------------------------------------------------------------------------
def clean3(list):                      #用函数回调实现数据去重
    def fn(callback):
        print("去重后的列表3为",callback(list))
    return fn
list3 = ['p','p','y','y','t','t','h','h','o','o','n','n','3','3']
@clean3(list3)
def cp(list):
    temp_list = []
    for num in list:
        if num not in temp_list:
            temp_list.append(num)
    return temp_list
#-----------------------------------------------------------------------------
temp_list = []                        #用函数递归实现数据去重
def clean4(list,num):
    if num == len(list):
        return
    elif list[num] not in temp_list:
        temp_list.append(list[num])
        clean4(list,num+1)
    else:
        clean4(list, num+1)
    return temp_list

list4 = ['S','S','K','K','T','T']
print("去重后的列表4为:",clean4(list4,0))


