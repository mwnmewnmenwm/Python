 # лабораторная работа №8
# (8 вариант)
### условие: 
![](https://i.imgur.com/df0jdZX.png)
![](https://i.imgur.com/CM0ifco.png)
### ход работы:
1. Импортируем необходимые модули.
2. Определяем пользовательские исключения: Invalid_URL_Exception, Request_Failed_Exception и Headlines_not_found, которые будут использоваться для обработки ошибок.
3. Создаем абстрактный класс WebScraper с абстрактными методами, предназначенными для создания веб-скрейперов.
4. Конкретный класс Modern_WebScraper наследует абстрактный класс WebScraper и реализует его абстрактные методы. Этот класс используется для извлечения данных с веб-страницы, в данном случае, заголовков новостей.
5. Класс RgbString содержит метод transformation, который используется для преобразования значений RGB в строку с кодом цвета в формате HEX.
6. Класс Create_window также наследует класс RgbString и содержит методы __init__ и run. В методе __init__ создается экземпляр Modern_WebScraper для получения данных с указанного URL-адреса, и заголовки новостей сохраняются в head_list. Далее создается графический интерфейс с использованием Tkinter. Метод run используется для отображения заголовков новостей в графическом окне.
7. В блоке if __name__ == '__main__': создается экземпляр класса Create_window, передавая URL-адрес в качестве аргумента, и вызывается метод run для запуска приложения.


### Результат вывода:
![](https://i.imgur.com/EvSOwG8.png)


## Список используемых источников:
### 1. [Имгур](https://imgur.com/)
### 2. [Tkinter в Python: создаем оконное GUI- приложение в 7 шагов](https://skillbox.ru/media/code/pishem-desktopprilozhenie-na-python-s-pomoshchyu-tkinter/)
### 3. [Python и Tkinter | окно приложения](https://metanit.com/python/tkinter/1.2.php)
### 4. [Скрапинг сайта с помощью Python: гайд для новичков](https://tproger.ru/translations/skraping-sajta-s-pomoshhju-python-gajd-dlja-novichkov)
### 5. [Веб-скрапинг с помощью Python](https://ru-brightdata.com/blog/how-tos-ru/web-scraping-with-python)
### 6. [Настройка полосы прокрутки в CSS](https://timeweb.cloud/tutorials/css-html/sozdanie-stilej-panelej-prokrutki-s-pomoshchyu-css)
