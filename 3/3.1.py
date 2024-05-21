# с рекурсией
def linearize(lst):
    result = [] # линейный список

    for item in lst:
        if isinstance(item, list): # если элемент список
            result.extend(linearize(item))
        else:
            result.append(item) # добавляем в результат
    return result

print("с рекурсией:")
print(linearize([1, 2, [3, 4, [5, [6, []]]]]))



# без рекурсии
def linearize_iterative(input_list):
    result = [] 
    stack = input_list

    while stack: 
        current = stack.pop() # извлекаем последний элемент
        if isinstance(current, list): # если элемент список
            stack.extend(current)
        else:
            result.append(current)
    return result

input_list = [1, 2, [3, 4, [5, [6, []]]]]
print("без рекурсии:")
print(linearize_iterative(input_list)[::-1])