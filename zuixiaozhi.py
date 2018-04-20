a=[999,666,66,33,55,41,10,34,1]
def min(a):
    n=len(a)
    j=n-1
    for i in range (0,j):
        if a[i]<a[i+1]:
            a[i+1]=a[i]
    return a[j]
print ("min="+str(min(a)))
