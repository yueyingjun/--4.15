def s(a,t=""):
    min = a[1]
    for j in range(2, len(a)):
        if a[j] < min:
            min = a[j]
            print(min)
    p = 0 #不同值的个数
    #将列表中每个值（重复的值取一次）连接成字符串
    for i in range(0,len(a)):
        k = 0
        for j in range(i + 1,len(a)):
            if a[j] == a[i]:
                k = 1
        if k == 0:
            t += str(a[i])+" "
            p += 1
    #将字符串中的数值用列表输出
    a = [0 for i in range(p)]
    i = 0
    j = 0
    while i < len(t):
        if t[i] != " ":
            z = ""
            while t[i] != " ":
                z += t[i]
                i += 1
            a[j] = int(z)
            j += 1
        else:
            i += 1
    return min,a
print(s([2,1,3,8,3,3,4,9]))

# 删除相同的数
def shanchu(a,i = 0):
    n = len(a)
    k = 0
    for j in range(i + 1,n - k):
        j = j - k
        if a[j] == a[i] and j < n - k:
            del a[j]
            k += 1
    i += 1
    if i < n:
        shanchu(a,i)
    return a
print(shanchu([2,1,3,8,3,3,4,9]))