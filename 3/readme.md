# лабораторная работа №3
# (8 вариант)
## 1 задание
### условие: 
![](https://i.imgur.com/agF4aAq.png)
### ход работы:
В обоих программах функция linearize() принимает список с вложенными списками и возвращает одномерный список всех элементов.

В программе с рекурсией функция проходит по каждому элементу списка. Если это элемент является списком, то функция рекурсивно вызывает себя для этого элемента. Таким образом, список разворачивается до тех пор, пока вложенных списков не останется, после чего элементы добавляются в результат.

В программе без рекурсии используется цикл, который проходит по списку в обратном порядке. Если элемент является списком, он добавляется в стек, который затем обрабатывается поочередно. Таким образом, все элементы списка добавляются в результат в правильном порядке.
### Результат вывода:
![](https://i.imgur.com/FO8ISUn.png)

## 2 задание
### условие: 
![](https://i.imgur.com/FT0YT4s.png) 
### ход работы:
В обоих программах рассчитывается значение a_k и b_k для k = 5, где значения a_k и b_k определяются по формулам, которые были даны.

В первой программе с использованием рекурсии, функции a_recursive и b_recursive рекурсивно вызывают друг друга для вычисления a_k и b_k. При этом, когда k достигает значения 1, происходит возврат некоторого начального значения.

Во второй программе без использования рекурсии, значения a_k и b_k рассчитываются с использованием массивов a и b. Начальные значения для a и b задаются, а затем в цикле происходит вычисление значений a[i] и b[i] на основе предыдущих значений a[i-1] и b[i-1] в соответствии с формулами.

После выполнения каждой программы выводятся значения a_k и b_k.

### Результат вывода:
![](https://i.imgur.com/1EyfZuD.png)



## Список используемых источников:
### 1. [Как работает рекурсия – объяснение в блок-схемах и видео](https://habr.com/ru/articles/337030/)
### 2. [Имгур](https://imgur.com/)