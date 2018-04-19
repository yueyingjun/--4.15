def quchong():
    arr = [1,2,3,3,4,2,3,4,5,6,1,9,9,7,8,6]
    news_arr = []
    for i in arr:
        if i not in news_arr:
            news_arr.append(i)
    return(news_arr)
print(quchong())