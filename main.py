'''
1) Координаты точки: Создайте кортеж point, содержащий координаты точки на плоскости.
Запросите у пользователя значения координат x и y и сохраните их в кортеже. Выведите
этот кортеж на экран.
'''
# x = float(input("Введите значение координаты x: "))
# y = float(input("Введите значение координаты y: "))
# point = (x, y)
# print(point)
'''
2) Информация о студенте: Создайте кортеж student_info, содержащий информацию о
студенте: имя, фамилия, возраст и средний балл. Запросите у пользователя эту
информацию и сохраните в кортеже. Выведите этот кортеж на экран.
'''
# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# age = int(input('Введите возраст: '))
# grades = int(input('Введите средний балл: '))
# student_info = (name, surname, age, grades)
'''
3) Месяцы года: Создайте кортеж months, содержащий названия месяцев года. Выведите
каждый месяц на отдельной строке.
'''
# months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
# for i in months:
#     print(i)
'''
4) Оценки: Создайте кортеж grades, содержащий оценки студента за несколько предметов.
Выведите среднюю оценку студента.
'''
# grades = (100, 100, 95, 100, 100, 100, 100, 100)
# summa = 0
# for i in grades:
#     summa += i
# av_grade = summa / len(grades)
# print(av_grade)
'''
1) Уникальные элементы: Создайте множество unique_numbers, содержащее уникальные
элементы из списка чисел. Выведите это множество на экран.
'''
# unique_numbers = {100, 100, 95, 100, 100, 100, 100, 100}
# print(unique_numbers)
'''
2) Пересечение множеств: Создайте два множества set1 и set2, содержащие некоторые
общие элементы. Выведите на экран их пересечение.
'''
# set1 = {100, 100, 95, 100, 112, 100, 100, 100}
# set2 = {110, 120, 95, 111, 100, 101, 100, 100}
# print(set1.intersection(set2))
'''
3) Объединение множеств: Создайте два множества set1 и set2, содержащие различные
элементы. Выведите на экран их объединение.
'''
# set1 = {100, 100, 95, 100, 112, 100, 100, 100}
# set2 = {110, 120, 95, 111, 100, 101, 100, 100}
# print(set1.union(set2))
'''
4) Разность множеств: Создайте два множества set1 и set2. Выведите на экран элементы,
которые содержатся только в set1, но не содержатся в set2.
'''
# set1 = {100, 100, 95, 100, 112, 100, 100, 100}
# set2 = {110, 120, 95, 111, 100, 101, 100, 100}
# print(set1.difference(set2))
'''
5) Подмножество: Проверьте, является ли одно множество подмножеством другого
множества.
'''
# set1 = {100, 100, 95, 100, 112, 100, 100, 100}
# set2 = {110, 120, 95, 111, 100, 101, 100, 100}
# print(set1.issubset(set2))
'''
1) Хранение информации о студентах: Создайте словарь student, содержащий
информацию о студенте (имя, возраст, оценки и т. д.). Выведите эту информацию на
экран.
'''
# student = {
#     'name': 'Соломон',
#     'age': 30,
#     'grades': [100, 100, 95, 100, 100, 100, 100, 100],
# }
# print(student)
'''
2) Поиск элемента по ключу: Создайте словарь phone_book, содержащий имена и номера
телефонов. По запросу имени выведите соответствующий номер телефона.
'''
# phone_books = {
#     'Aitunuk': '0551551794',
#     'Solomon': '0220000018',
#     'Emir': '0772152383'
# }
# request = input('Введите имя: ')
# print(phone_books[request])
'''
3) Сумма значений: Создайте словарь expenses, содержащий расходы по различным
категориям (например, "еда", "транспорт" и т. д.). Вычислите общую сумму расходов.
'''
# expenses = {
#     'food': 10000,
#     'Aitunuk': 10000,
#     'Codify': 13000,
#     'Others': 13000
# }
# summa = 0
# for key, values in expenses.items():
#     summa += values
# print(summa)
'''
4) Обновление значения: Создайте словарь inventory, содержащий информацию о
количестве товаров на складе. Обновите количество определенного товара на складе и
выведите обновленную информацию.
'''
# inventory = {
#     'iphone': 15,
#     'ipad': 10,
#     'macbook': 17,
#     'Homepod': 5
# }
# inventory['macbook'] = 10
# inventory['Homepod'] = 10
# print(inventory)
'''
5) Удаление элемента: Создайте словарь grades, содержащий оценки студентов по
различным предметам. Удалите оценку определенного студента и выведите
обновленную информацию.
'''
# grades = {
#     'Solomon': {'math': 5, 'physics': 4, 'russian': 2},
#     'Omurbek': {'math': 5, 'physics': 4, 'russian': 2}
# }
# grades['Solomon'].pop('math')
# print(grades)
'''
    Кортеж - 30 б.
1) Названия дней недели: Создайте кортеж days_of_week, содержащий названия дней недели.
Выведите дни недели на экран в обратном порядке.
'''
# days_of_week = ('Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# print(days_of_week[::-1])
'''
2) Геометрические фигуры: Создайте кортеж shapes, содержащий названия геометрических
фигур (например, квадрат, треугольник, круг и т. д.). Запросите у пользователя название
фигуры и выведите её на экран.
'''
# shapes = ('Квадрат', 'Треугольник', 'Круг', 'Овал')

# user_data = input('Введите геометрическую фигуру: ')
# via_index = shapes.index(user_data)

# if user_data in shapes:
#     print(shapes[via_index])
# else:
#     print('Такого нет')
'''
3) Сезоны года: Создайте кортеж seasons, содержащий названия сезонов года.
Выведите сезоны года на экран в алфавитном порядке.
'''
# seasons = ('Зима', 'Весна', 'Лето', 'Осень')
# result = sorted(seasons)
# print(result)
'''
4) Номера месяцев: Создайте кортеж month_numbers, содержащий номера месяцев от 1 до 12.
Запросите у пользователя номер месяца и выведите название этого месяца.
'''
# month_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# months_names = ['Январь', 'Февраль', 'Март', 'Апрель','Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

# user = int(input("Введите номер месяца от 1 до 12: "))

# index = month_numbers.index(user)
# name = months_names[index]

# if user in month_numbers:
#     print(name)
# else:
#     print("Такого месяца нет!")

'''
5) Температуры: Создайте кортеж temperatures, содержащий значениятемператур
в течение дня. Выведите минимальную и максимальную температуры.
'''
# temperatures = (2, 2, 1, -2, -2, -2)
# print('Максимальная температура: ', max(temperatures))
# print('Минимальная температура: ', min(temperatures))
'''
6) Пары чисел: Создайте кортеж number_pairs, содержащий пары чисел.
Вычислите сумму всех пар чисел.
'''
# numbers_pairs = ((1, 2), (3, 4), (5, 6), (7, 8))
# pairs_sum = sum(numbers_pairs)

# print("Сумма всех пар чисел: ", pairs_sum)

'''
Множество - 30 б.
1) Удаление дубликатов: Удалите дубликаты из списка, преобразовав его в множество.
'''
# numbers = {1, 2, 3, 4, 2, 3, 5, 6, 1}
# result = set(numbers)
# print(result)
'''
2) Подсчёт уникальных слов: Создайте множество слов из строки текста
и выведите количество уникальных слов.
'''
# text = 'Подсчёт уникальных слов: Создайте множество слов из строки текста и выведите количество уникальных слов.')
# words_set = set(text.split(' '))
# print("Количество уникальных слов: ", len(words_set))
'''
3) Сравнение множеств: Проверьте, содержат ли два множества одни и те же элементы.
'''
# nums1 = {1, 2, 3, 4, 5}
# nums2 = {3, 4, 5, 6, 7}
# same_numbers = nums1 & nums2
# print(same_numbers)
'''
4) Удаление элемента из множества: Удалите определенный элемент из множества.
'''
# nums = {1, 2, 3, 4, 5}
# user_data = int(input('Введите число: '))
# nums.remove(user_data)
# print(nums)
'''
5) Поиск пересечения в строках: Найдите все общие символы в двух строках
и выведите их в виде множества.
'''
# text1 = 'Найдите все общие символы в двух строках'
# text2 = 'и выведите их в виде множества'
# new1 = set(text1)
# new2 = set(text2)
# result = new1.intersection(new2)
# result.remove(' ')
# print('Общие символы: ', result)
'''
Словарь - 40 б.
1) Подсчет частоты элементов: Создайте словарь word_count, содержащий частоту
встречаемости слов в тексте. По запросу слова выведите количество его вхождений
'''
# ?????????
'''
2) Проверка наличия ключа: Проверьте, есть ли определенный ключ в словаре.
'''
# catalog = {'a': 1, 'b': 2, 'c': 3}
# req = input('Поиск: ')
# if req in catalog.keys():
#       print(f"Ключ {req} найден в словаре: {catalog[req]}")
# else:
#     print(f"Ключ {req} не найден в словаре.")
'''
3) Извлечение значений: Извлеките все значения из словаря
и сохраните их в отдельный список.
'''
# catalog = {'a': 1, 'b': 2, 'c': 3}
# result = set(catalog.values())
# print(*result)
'''
4) Объединение словарей: Объедините два словаря в один.
'''
# cat1 = {'a': 1, 'b': 2}
# cat2 = {'b': 3, 'c': 4}
# cat1.update(cat2)
# print(cat1)
'''
5) Сортировка словаря: Отсортируйте словарь по ключам или значениям
и выведите результат
'''
# catalog = {'a': 1, 'c': 3, 'b': 2}
# sorted_keys = dict(sorted(catalog.keys()))
# sorted_value = dict(sorted(catalog.values()))
# print("Отсортированный словарь по ключам:", sorted_keys)
# print("Отсортированный словарь по значениям:", sorted_value)
