my_family = ['Мама', 'Папа', 'Брат','Сестра']
my_family_height = [
    ['Мама', 160],
    ['Папа', 182],
    ['Брат', 110],
    ['Сестра', 155]
]
for i in my_family_height:
    if i[0] == 'Папа':
        print(f"Рост отца - {i[1]} см")
sum_height = sum([i[1] for i in my_family_height])
print(f"Общий рост моей семьи - {sum_height} см")
 
