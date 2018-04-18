a=[9,1,8,3,1,3,7,5,6,8,9,2,2,10]
def math(a):
    for j in range (len(a)-1,0,-1):
        temp = a[j]
        for i in range (0,j):
            if a[i] == temp:
                if j<len(a)-1:
                    a.pop(j)
                else:
                    a.pop()
    return a
print (math(a))







