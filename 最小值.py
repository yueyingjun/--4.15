list=[23,243,1,67,123,3]
def zuixiaozhi(min):
    temp=min[0]
    for i in range(len(min)):
        if temp>min[i]:
            temp=min[i]
    return temp

print(zuixiaozhi(list))

