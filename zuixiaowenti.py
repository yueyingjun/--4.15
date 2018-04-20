arr=[59,6,42,33,3,47,12,37]
for i in range (0,len(arr)-1):
        j=i+1
        if arr[i]<arr[j]:
            temp=arr[j]
            arr[j]=arr[i]
print(arr[i])
