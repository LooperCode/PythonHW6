def ProgMath (n, d, array, fst):
    while n != 0:
        array.insert(0, fst + (n-1) * d)
        n-=1
        
    return array

n = int(input("Введите размер массива: "))
d = int(input("Введите разность: "))
fst = int(input("Введите значение первого элемента: "))
array = []
array = ProgMath(n, d, array, fst)

print(array)
  