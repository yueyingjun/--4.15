def qiumax(a):
    for i in range(1,len(a)):
        if a[i]>a[i-1]:
            temp=a[i]
        else:
            temp=a[i-1]
    return temp

print(qiumax([6,4,3,1,7,0]))
