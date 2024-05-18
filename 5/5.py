def apply_func(seq, func, n): 
    def apply_n(result):
        for _ in range(n):
            result = func(result)
        return result
    
    def znachitelno_izmeneno(original, changed): #для сравнения
        return (changed - original) >= 10
    
    izmenenie_elements = map(apply_n, seq) #применяю функцию к каждому элементу
    filtered_elements = filter(lambda x: znachitelno_izmeneno(x[0], x[1]), zip(seq, izmenenie_elements))
    
    for _, changed in filtered_elements:
        yield (changed) #генератор

original = [1, 7, 5, 17, 10] 
n = 3 #кол-во повторов

filtered_changed_elements = apply_func(original, lambda x: x*2, n) #функ-я к посл-ти

for element in filtered_changed_elements:
    print(element)
