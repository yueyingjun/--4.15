arr=[59,6,37,33,3,47,3,37]
def stars(arr):
    for i in arr:
        while arr.count(i)>1:
            del arr[arr.index(i)]
    return arr
print(stars(arr))
