a=[1,5,7,8,9,5,88,7,4,5,82,3,5,1,2,3,5]
a.sort()
y=a[-1]
for x in range(len(a)-2,-1,-1):
    if y==a[x]:
        a.remove(a[x])
    else:
        y=a[x]
print(a)





