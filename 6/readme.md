 # лабораторная работа №6
# (8 вариант)
### условие: 
![](https://i.imgur.com/ggse3QS.png)
![](https://i.imgur.com/kgNlAtF.png)
### ход работы:
#### Основная программа:
tkinter для создания графического интерфейса.
messagebox для вывода информационных сообщений.
calculate_recipe и create_docx_report для осуществления расчётов и создания отчета.
calculate_and_save(): собираем информацию о выбранном рецепте и введённых количествах ингредиентов, затем вызывает функции расчёта и создания отчёта.
create_entries(ingredients): создаем поля для ввода количества ингредиентов в соответствии с выбранным рецептом.
update_entries(*args): обновляем список ингредиентов в зависимости от выбранного рецепта.

Создаем основного окна приложения. Создаем кнопки для выбора рецепта. Создаем кнопку "Рассчитать и сохранить". Создаем метки для отображения результатов расчёта.

#### Модуль ingredients: 
Содержит данные в виде словаря об ингредиентах, их цен и калорийности на 100 гр.
#### Модуль calculator:
Функция принимает словарь с ингредиентами и их количеством, затем рассчитывает энергетическую ценность и стоимость рецепта, используя данные из словаря INGREDIENTS.
#### Модуль report:
Функция create_docx_report создает отчёт в формате docx с информацией о рецепте (название, ингредиенты и их количество, энергетическая ценность, стоимость).

Основная программа использует функции из модулей recipes для расчёта и создания отчётов.
Модули recipes используют данные из модуля ingredients для расчёта питательной ценности и стоимости ингредиентов.

### Результат вывода:
![](https://i.imgur.com/UdYf1HF.png)
![](https://i.imgur.com/Z6Picpo.png)

## Список используемых источников:
### 1. [Имгур](https://imgur.com/)
### 2. [Tkinter в Python: создаем оконное GUI- приложение в 7 шагов](https://skillbox.ru/media/code/pishem-desktopprilozhenie-na-python-s-pomoshchyu-tkinter/)
### 3. [Python и Tkinter | окно приложения](https://metanit.com/python/tkinter/1.2.php)