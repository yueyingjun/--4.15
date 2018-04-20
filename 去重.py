list=[1,1,2,0,3,5,2]
def quchong(list):
    lists = [list[0]]

    for i in list [0:]:
        if i not in lists:
            lists.append(i)

    return lists

print(quchong(list))
