abc=[]
def bb(arr):
    for i in arr:
        if(i not in abc):
            abc.append(i)
    return abc
cc=[12,2,3,2,4,3]
print("去重后的列表是:",bb(cc))

