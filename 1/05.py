zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, 'bear')
print(zoo)
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)
zoo.remove('elephant')
print(zoo)
print(f"Лев сидит в клетке {zoo.index('lion') + 1}, а жаворонок сидит в клетке {zoo.index('lark') + 1}.")
