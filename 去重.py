list=[2,3,5,4,5,3,4,5]
def quchong(data):
    newlist = [list[0]]
    for i in data[1:]:
        if i not in newlist:
            newlist.append(i)
    return newlist

print(quchong(list))