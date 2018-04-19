def min(a,temp=1):
    b=len(a)
    for x in range(0,b):
        for y in range(x+1,b):
            if temp==1:
                if a[x] < a[y]:
                    c = a[x]
                    a[x] = a[y]
                    a[y] = c
            else:
                if a[x] > a[y]:
                    c = a[x]
                    a[x] = a[y]
                    a[y] = c
    return a[y]
a=[3,1,23,45,13,44,12,56,67,4]
print(min(a,2))