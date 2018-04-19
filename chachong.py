b = [9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]
def aaa(b):
    n = len(b)
    k = 0
    for i in range(0,n-k):
        for j in range(i+1,n-k):
            if n-k>i and n-k>j and b[i] == b[j]:
                del (b[j])
                k = k+1
                if n-k>j and b[i] == b[j]:
                    del(b[j])
                    k = k+1
                    if n-k>j and b[i] == b[j]:
                        del (b[j])
                        k = k+1
            else:
                continue
    return b
print(aaa(b))
