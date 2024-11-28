def bubblesort(datalist):
    n = len(datalist)
    for i in range(n):
        for j in range(n-i-1):
            if datalist[j] > datalist[j+1]:
                datalist[j], datalist[j+1] = datalist[j+1], datalist[j]
datalist = [1, 5, 4, 3, 7, 8, 9]
bubblesort(datalist)
print(datalist)
