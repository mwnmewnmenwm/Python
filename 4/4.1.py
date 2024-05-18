def average_closure():
    numbers = [] # для хранения чисел

    def add_number(num): #замыкание
        numbers.append(num)
        avg = sum(numbers) / len(numbers) #вычисляем среднее
        return avg

    return add_number

avg_func = average_closure() 
print(avg_func(7))
print(avg_func(20))
print(avg_func(48))
print(avg_func(2))