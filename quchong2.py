#第一次交的去重是有错误的，这次是修改之后的去重
a=[1,9,1,8,2,3,1,3,7,5,1,6,100,668,9,2,2,2,9]
def math(a):
    for j in range (len(a)-1,0,-1):
        temp = a[j]
        i=0
        while i <j :
            if a[i] == temp:
                if j<len(a)-1:
                    a.pop(j)
                else:
                    a.pop()
                break
            i=i+1

    return a
print (math(a))