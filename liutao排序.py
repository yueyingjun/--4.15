#查重
a=[3,3,2,3,2,1,2]
def chachong(a):
    i=0
    n=len(a)
    k=0
    while i<n-1:
        for j in range(i+1,n-k):
            j=j-k
            if a[i]==a[j]:
                del a[j]
                k+=1
        i+=1
    return a
print(chachong(a))


#最值
lb1=[7,5,3,3,2]
def short(lb,temp=1):
    for i in range(len(lb)):
        for j in range(i+1,len(lb)):
            if temp==1:
                if lb[j]<lb[i]:
                    n=lb[i]
                    lb[i]=lb[j]
                    lb[j]=n
            else:
                if lb[j]>lb[i]:
                    n=lb[i]
                    lb[i]=lb[j]
                    lb[j]=n
    return lb;
print(short(lb1)[0])