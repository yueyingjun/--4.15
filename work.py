#去重
a = [1, 3, 9, 3, 5, 4, 7, 5, 6, 8, 9, 2, 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)



#最小值
a=[6,9,52,33,225,6,253,25,48,52,23]
for i in range(len(a)):
    if a[0]>a[i]:
        k=a[0]
        a[0]=a[i]
        a[i]=k
print(a[0])
