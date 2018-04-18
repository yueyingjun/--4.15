def mix(l):
    for i in range (1,len(l)):
        if l[0]>l[i]:
            l[0]=l[i]
    return l[0]
x=[5,8,8,8,8,7,7,4,4]



def chachong(x):
    for i in range (len(x)-1,0,-1):
        for j in range (0,i):
            if  x[j]==x[i]:
                x.remove(x[j])
    return x

print(chachong(x))
