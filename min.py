list = [99,88,77,6,55,44,33,22,11]
def min(list):
    n = len(list)
    if list[0]<list[1]:
                temp = list[0]
    else:
                temp = list[1]
    for i in range(2, n):
        if temp < list[i]:
            temp = temp
        else:
            temp = list[i]

    return temp
print(min(list))