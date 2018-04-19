def remove(b):
    a = [3, 4, 2, 4, 2, 5, 63, 3, 1]
    for x in a:
        if x not in b:
            b.append(x)
    return b
b=[]
print(remove(b))
