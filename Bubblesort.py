f_name = input ("Enter your first name ")
l_ name = input ("Enter last name ")
print ( f "Your full name is {f_name} {l_name}")
def bubblesort (datalist) :
    n = len (datalist)
    for i in range (n) :
        for j in range (n-i-1) :
            if datalist [j] > datalist[j+1] :
                datalist [j] , datalist [j+1] = datalist [j+1], datalist [j]
datalist= [1,5,4,3,7,8,9]
print (bubblesort(datalist))
