import random
def IntervalSrch (array, min, max, n):
    resultList = []
    for i in range(n): 
        array.insert(i, random.randint(0, 15))
        if array[i] >= min and array[i] <= max:
            resultList.append(i)
    return resultList    
            
      
min = int(input("Введите минимальное значение диапозона: "))
max = int(input("Введите максимальное значение диапозона: "))
n = 10
array = []
print(IntervalSrch(array, min, max, n))   
