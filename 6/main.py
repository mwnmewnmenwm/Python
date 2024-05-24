import tkinter as tk
from tkinter import messagebox
from recipes.calculator import calculate_recipe
from recipes.report import create_docx_report

def calculate_and_save():
    selected_recipe = recipe_var.get() # рецепт
    recipe = {} # ингредиенты и их количество
    for ingredient, widgets in entries.items():
        entry = widgets[1]
        recipe[ingredient] = float(entry.get())
    
    total_calories, total_cost = calculate_recipe(recipe)
    result_text.set(f'Энергетическая ценность: {total_calories} ккал\nСтоимость: {total_cost} руб.')
    create_docx_report(selected_recipe, recipe, total_calories, total_cost)
    messagebox.showinfo('Информация', 'Отчет успешно создан!')

root = tk.Tk()
root.title("Калькулятор рецептов")

recipe_var = tk.StringVar(value='Пицца')

tk.Label(root, text="Выберите рецепт:").pack() # кнопка для выбора рецепта
tk.Radiobutton(root, text="Пицца", variable=recipe_var, value='Пицца').pack()
tk.Radiobutton(root, text="Бургер", variable=recipe_var, value='Бургер').pack()
tk.Radiobutton(root, text="Вок", variable=recipe_var, value='Вок').pack()

entries = {}

def create_entries(ingredients):

    for widgets in entries.values():
        widgets[0].destroy()  
        widgets[1].destroy()  
    entries.clear()
    
    for ingredient in ingredients:
        label = tk.Label(root, text=f"{ingredient} (г):")
        label.pack()
        entry = tk.Entry(root)
        entry.pack()
        entries[ingredient] = (label, entry)

def update_entries(*args): # тут будут менятся ингредиенты 
    selected_recipe = recipe_var.get()
    if selected_recipe == 'Пицца':
        create_entries(['тесто', 'сыр', 'колбаса'])
    elif selected_recipe == 'Бургер':
        create_entries(['булка', 'котлета', 'сыр'])
    elif selected_recipe == 'Вок':
        create_entries(['лапша', 'курица', 'сыр'])

recipe_var.trace('w', update_entries)

button_calculate = tk.Button(root, text="Рассчитать и сохранить", command=calculate_and_save)
button_calculate.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

root.mainloop() # необходимо дял запуска
