def shanchong(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                a[j]=None
    while None in a:
        a.remove(None)
    return(a)

print(shanchong([1,2,2,2,4,2,5]))