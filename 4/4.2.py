
def argument_checker(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)): # проверка на тип
                raise TypeError("Аргумент должен быть числом (int или float)")

            if arg < 0 or arg > 100: # проверка на диапазон
                raise ValueError("Значение аргумента должно быть от 0 до 100")

        return func(*args) #
    return wrapper

@argument_checker #декоратор
def multiply(a, b):
    return a * b

try:
    print(multiply(17, 10))
except (TypeError, ValueError) as e: #если есть искл. выводим ошибку
    print(f"Ошибка: {e}")
