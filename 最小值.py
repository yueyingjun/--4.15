lists=[4,2,3,0,4,5,1]
def zuixiaozhi(lists):
    min=lists[0]
    for i in range (0,len(lists)):
            if lists[i]<min:
                min=lists[i]

    return min
print(zuixiaozhi(lists))