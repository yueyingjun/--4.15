def min(a):
    h=len(a)
    for x in range(0,h):
        for y in range(x,h):
            if a[x]>a[y]:
                m=a[x]
                a[x]=a[y]
                a[y]=m
    print(a[0])

