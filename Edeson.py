#=============================================================================
#-     -   -  -  -  - - ---Условия, циклы и рекурсии--- - -  -  -  -   -     -
#=============================================================================
'''
В зоопарке цена входного билета зависит от возраста
посетителя. Дети до двух лет и пенсионеры старше 65 лет
допускаются бесплатно. Дети в возрасте от трех до 12 лет
могут посещать зоопарк за 200 рублей. Обычный взрослый билет стоит 500 рублей.

Напишите программу, которая будет запрашивать
возраст всех посетителей в группе по одному за раз
и выводить общую цену билетов для посещения зоопарка
этой группой. Общую цену билетов стоит выводить в
формате с двумя знаками после запятой.
'''
# def total_sum():
#     total_price = 0
#     person_old = 0
#
#     print('Для остановки программы напишите "-1" при вводе возраста человека')
#
#     while person_old != -1:
#         person_old = int(input('\nВведите возраст человека: '))
#         if person_old <= 2 or person_old > 65:
#             total_price += 0
#             print(f'Общая сумма: {total_price:.2f} руб.')
#         elif person_old >= 3 and not person_old > 12:
#             total_price += 200
#             print(f'Общая сумма: {total_price:.2f} руб.')
#         else:
#             total_price += 500
#             print(f'Общая сумма: {total_price:.2f} руб.')
#
#     print(f'\n\nИтоговая общая сумма: {total_price:.2f} руб.\nЗавершение программы!')
#
#
# total_sum()
#
# def total_sum():
#     total_price = 0
#     print('Для остановки программы напишите "-1" при вводе возраста человека')
#
#     while True:
#         user_input = input('\nВведите возраст человека: ').strip()
#
#         # Проверка на завершение
#         if user_input == "-1":
#             break
#
#         # Проверка, что введено число
#         if not user_input.isdigit():
#             print("Ошибка: введите положительное число или -1 для выхода.")
#             continue
#
#         age = int(user_input)
#
#         # Расчёт стоимости билета
#         if age <= 2 or age > 65:
#             price = 0
#         elif 3 <= age <= 12:
#             price = 200
#         else:
#             price = 500
#
#         total_price += price
#         print(f'Общая сумма: {total_price:.2f} руб.')
#
#     print(f'\nИтоговая сумма за всех: {total_price:.2f} руб.\nЗавершение программы.')
#
# total_sum()

'''
Юлию Цезарю необходимо было посылать секретные
письменные приказы своим генералам. В результате
он стал шифровать свои послания довольно простым
методом, который теперь называют кодом Цезаря.
Идея шифрования заключалась в циклическом сдвиге
букв на три позиции. В итоге буква A превращалась в D,
B – в E, C – в F и т. д. Последние три буквы алфавита
переносились на начало. Таким образом, буква X
становилась A, Y – B, а Z – C.
Цифры и другие символы не подвергались шифрованию.

Важно: буквы идут по алфавиту в кодировке Юникод.
Большие и маленькие буквы находятся в кодировке
в разных местах, поэтому обрабатывать переход нужно
отдельно для заглавных и строчных букв.
Для проверки символов можно использовать функции
isalpha() — буква ли это, и isupper() — заглавная ли
это буква.
Напишите программу, которая реализует код Цезаря
для латинского алфавита. Позвольте пользователю
ввести фразу, после чего выведите результат.
'''
# def cezar_code():
#     lowercase_letters = [
#         'a', 'b', 'c', 'd', 'e', 'f', 'g',
#         'h', 'i', 'j', 'k', 'l', 'm', 'n',
#         'o', 'p', 'q', 'r', 's', 't', 'u',
#         'v', 'w', 'x', 'y', 'z'
#     ]
#     uppercase_letters = [
#         'A', 'B', 'C', 'D', 'E', 'F', 'G',
#         'H', 'I', 'J', 'K', 'L', 'M', 'N',
#         'O', 'P', 'Q', 'R', 'S', 'T', 'U',
#         'V', 'W', 'X', 'Y', 'Z'
#     ]
#     text = input('Введите текст для шифровки: ')
#     text_new = []
#     for letter in text:
#         if letter.isalpha():
#             if letter.isupper():
#                 if letter not in ['X', 'Y', 'Z']:
#                     i = uppercase_letters.index(letter)
#                     i += 3
#                     text_new.append(uppercase_letters[i])
#                 else:
#                     i = uppercase_letters.index(letter)
#                     i -= 23
#                     text_new.append(uppercase_letters[i])
#             else:
#                 if letter not in ['x', 'y', 'z'] :
#                     i = lowercase_letters.index(letter)
#                     i += 3
#                     text_new.append(lowercase_letters[i])
#                 else :
#                     i = lowercase_letters.index(letter)
#                     i -= 23
#                     text_new.append(lowercase_letters[i])
#         else:
#             text_new.append(letter)
#
#     return ''.join(text_new)
#
#
# print(cezar_code())

'''
Изучите список:

a = [1, 1, 2, 3, 5, 8, 34, 55, 89].

Напишите код: выведите все элементы списка, которые
меньше 5.
'''
# a = [1, 1, 2, 3, 5, 8, 34, 55, 89]
# b = []
# for i in a:
#     if i < 5:
#         b.append(i)
# print(b)

'''
Напишите программу: запросите у пользователя целое
число и выведите на экран информацию о том, четное
оно или нечетное.
'''
# def check_num():
#     number = int(input(f'Введите число: '))
#     return 'четное' if number % 2 == 0 else 'нечетное'
#
# print(check_num())

'''
Напишите программу для отображения стандартной
таблицы умножения от единицы до десяти. Убедитесь, 
что ваша таблица умножения имеет заголовки над первой строкой и слева от первого столбца.

Важно: в этом задании вам нужно выводить значения 
на экран без принудительного перевода курсора 
на строку ниже. Для этого задайте end="" в качестве
последнего аргумента функции print.

Например, функция print("A") выведет на экран букву
A, после чего автоматически перейдет на новую строку.
Так print("A", end="") не станет переводить курсор, 
и позволит произвести следующий вывод в той же строке.
'''
# for i in range(1, 11):
#     print(f"{i:>2}", end="")  # заголовок слева
#     for j in range(2, 11):
#         print(f"{i * j:>4}", end="")  # красиво выравненное тело
#     print()  # перенос строки

'''
Для выигрыша главного приза нужно, чтобы 6 номеров
на лотерейном билете совпали с шестью числами,
которые выпали случайным образом в диапазоне от 1 до 49. 

Напишите программу, которая будет случайным образом
подбирать шесть номеров для вашего билета. Убедитесь,
что среди этих чисел не будет дубликатов. Выведите
номера билетов на экран по возрастанию.

Важно: в коде используйте функцию random.sample().
'''
# import random
# ticket = random.sample(range(1, 50), 6)
# ticket.sort()
#
# print("Ваши лотерейные номера:", ticket)

'''
Напишите программу, которая будет запрашивать
у пользователя целочисленные значения и сохранять
их в виде списка. 

Чтобы закончить ввод значений, пользователь должен
ввести 0. 

Затем программа выведет на экран все числа, кроме 0,
в порядке возрастания — по одному значению в строке.
'''
# list_ = []
# number = True
#
# while number != 0:
#     number = int(input('Введите число: '))
#     list_.append(number)
#
# list_.remove(0)
# list_.sort()
# for i in list_:
#     print(i)

'''
Гарри, Рон и Гермиона отправляются на поиски крестражей. Как им удалось узнать, 
один из крестражей спрятан в хранилище Гринготтса — специального банка для волшебников.

Друзья приняли решение использовать зелье невидимости. Лучше всего это зелье работает в туманную погоду.

Помогите волшебникам выбрать дни для поиска крестражей. Создайте функцию search_day(), 
которая посчитает количество туманных дней в списке. 
Она принимает в качестве аргумента список с предположительной влажностью воздуха на ближайшие пять дней. 
Например, такой: 76, 89, 91, 32, 10. Если влажность превышает 80%, день считается туманным. 
Верните список с порядковыми номерами туманных дней. Номера дней считайте с нуля.
'''
# def search_day(humidity_list):
#     result = []
#     for index, humidity in enumerate(humidity_list):
#         if humidity > 80:
#             result.append(index)
#     return result
#
#
# humidity_list = [76, 89, 91, 32, 10]
#
#
# print(search_day(humidity_list))

'''
Теперь, когда волшебники определились с днем, в который они проникнут в Гринготтс, 
им необходимо распределить задачи между собой. Гермиона составила список задач:

Приготовить зелье невидимости.
Собрать вещи и подготовить снаряжение.
Раздобыть оборотное зелье.
Чтобы распределить задачи честно, Гермиона заколдовала три стакана с водой. 
Если дотронуться до стакана волшебной палочкой, вода в нем поменяет цвет.
 
Каждому цвету соответствует своя задача:
— если цвет окажется красным, то волшебник займется первой задачей;
— если цвет окажется синим, то волшебник займется второй задачей;
— если цвет окажется зеленым, то волшебник займется третьей задачей;
— если волшебнику выпадет любой другой цвет, значит, заклинание сработало некорректно.

Напишите программу, которая поможет волшебникам определить, какой задачей им нужно заняться. 
Создайте функцию task_check(), которая принимает на вход строку с названием цвета. 
Цвета передаются на английском языке. Функция должна вернуть номер задачи, 
которой соответствует цвет, или ноль, если цвету не соответствует ни одна задача.
'''
# def task_check():
#     task_colors = {
#         'red' : 1,
#         'blue' : 2,
#         'green' : 3
#     }
#     color = input('Введите название цвета на английском: ')
#     return task_colors.get(color, 0)
#
# print(task_check())

'''
Гермионе выпала первая задача — она должна приготовить зелье невидимости. 
У этого зелья несложный рецепт, но нужно быть очень внимательной.

Гермионе нужно помешивать зелье конкретное количество раз, чтобы оно получилось правильным. 
Она помечает все помешивания на пергаменте. 
Общее количество помешиваний должно соответствовать одному из условий:

— делится на 4 и не делится на 100;

— делится на 400.

Напишите функцию potion_check(), которая проверит, помешала ли Гермиона зелье правильное количество раз. 
Она должна принимать на вход один аргумент — число, которое обозначает, сколько раз Гермиона помешала зелье. 
В качестве результата работы функции верните yes, если количество помешиваний верное, или no в обратном случае. 
Используйте операторы and и or, чтобы скомбинировать несколько условий в одном if.
'''
# def potion_check(n):
#     return 'yes' if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0 else 'no'
#
#
# n = 399
#
# print(potion_check(n))

'''
Рону досталась вторая задача — собрать вещи и подготовить снаряжение. Рон составил список необходимых вещей:

— мантия-невидимка;
— волшебная палочка;
— набор зелий;
— карта;
— оберег от проклятий.

Рон не очень внимательный и боится забыть что-то важное и взять что-то лишнее. 
Помогите ему — создайте функцию importance_check(), которая проверит, нужно ли брать предмет с собой. 
Она принимает на вход один аргумент — название предмета, который можно взять. 
Названия предметов передаются на русском языке, все необходимые предметы называются так же, как они названы в списке выше. 
Если предмет входит в список и его нужно взять, верните 1. Если не входит — значит, брать его не нужно, верните 0.
'''

# def importance_check(item):
#     return int(item in ['мантия-невидимка', 'волшебная палочка', 'набор зелий', 'карта', 'оберег от проклятий'])
#
# item = 'мантия-'
#
# print(importance_check(item))

'''
Известно, что фамилии всех студентов Дурмстранга в Лютном переулке оканчиваются "ов". 
Создайте функцию student_suspect(), которая определит, подходящая ли фамилия у предполагаемого студента. 
Функция принимает на вход один аргумент — строку с фамилией студента. 
Если фамилия оканчивается на "ов", верните «Лови!». 
В любом ином случае верните «Пропусти его»
'''
# def student_suspect(text):
#     return 'Лови!' if text[-2:] == 'ов' else 'Пропусти его'
#
# text = 'Кабшанов'
#
# print(student_suspect(text))

'''
На каждой двери есть номер из четырех цифр. Если номер является палиндромом, то дверь безопасна. 
Палиндром — это строка, которая одинаково читается в обоих направлениях. 
Например, строка «1331» — это палиндром.

Напишите функцию security_check(), которая проверит, безопасно ли выходить через определенную дверь. 
Функция принимает один аргумент — строку с последовательностью цифр на двери. 
Проверьте, является ли строка палиндромом. 
Если да, то верните «Безопасно». В любом ином случае верните «Ловушка».
'''
# def security_check(text):
#     return 'Безопасно' if text[::-1][0:2] == text[:2] else 'Ловушка'

'''
КиберКодер — известный в узких кругах хакер. Уже много лет его занимает одна задача. 
Он хочет взломать шифр, за которым прячется ответ на главный вопрос Вселенной. 
КиберКодеру очень бы пригодилась ваша помощь.

Для первого этапа взлома КиберКодеру нужно подобрать номера портов сервера, к которым он сможет подключиться. 
Известно, что это четные числа, которые находятся в определенном диапазоне.

Напишите функцию even_numbers(), которая найдет все четные числа в диапазоне. 
Она принимает два аргумента — начало и конец промежутка, внутри которого нужно будет найти четные цифры. 
Сохраните в список все четные числа в заданном диапазоне и верните этот список в качестве ответа.
'''
# def even_numbers(a, b):
#     even = []
#
#     for i in range(a, b+1):
#         if i % 2 == 0:
#             even.append(i)
#
#     return even
#
# a = 1
# b = 10
#
# print(even_numbers(a, b))

'''
Создайте функцию directories_check(), которая принимает один аргумент — список целых чисел. 
Каждое число в этом списке — это номер директории. 
Функция должна сохранить все нечетные номера в отдельный список и вернуть его в качестве ответа. 
Если в исходном списке встретилась директория с номером 359, 
остановите проверку и сохраните только те нечетные числа, которые попали в список до 359. 
Число 359 не должно попасть в ответ.
'''
# def directories_check(list_):
#     even_list = []
#
#     for i in list_:
#         if i == 359:
#             break
#         if i % 2 != 0:
#             even_list.append(i)
#
#     return even_list
#
#
# list_ = [2, 4, 6, 8, 10]

'''
Создайте функцию crosscheck(), которая принимает на вход два аргумента — два списка целых чисел. 
Функция должна найти числа, которые есть сразу в двух списках. 
В качестве ответа верните список этих чисел. Используйте циклы для решения задачи.
'''
# list_number_1 = [3, 7, 12, 5, 9, 21, 14, 8, 18, 11]
# list_number_2 = [5, 9, 14, 22, 3, 17, 25, 11, 30, 7]
#
# def crosscheck(list1, list2):
#     joint_number  = []
#
#     for i in list1:
#         if i in list2:
#             joint_number.append(i)
#
#     return joint_number
#
#
# print(crosscheck(list_number_1, list_number_2))

'''
Создайте функцию unique_key(), которая принимает один аргумент — целое положительное число. 
Функция unique_key должна найти сумму всех цифр числа из аргумента. 
Верните эту сумму в качестве ответа. Используйте цикл while для решения задачи.
'''
# Создайте функцию unique_key
# def unique_key(number):
#         # Создайте переменную, в которой сохраните итоговую сумму
#     digit_sum = 0
#
#     # Используйте цикл while, чтобы разбить число на цифры.
#     # Пока в числе еще есть цифры, действия будут повторяться.
#     while number > 0:
#             # Получите последнюю цифру числа
#         digit = number % 10
#         # Добавьте полученную цифру к итоговой сумме
#         digit_sum += digit
#         # Удалите цифру, которую вы обработали, из числа
#         number //= 10
#
#     # Верните сумму цифр числа в качестве ответа
#     return digit_sum
#
# a=538
#
# print(unique_key(a))

'''
Создайте функцию count_letters(), которая посчитает, сколько раз буква повторяется в строке. 
Функция должна принимать два аргумента — строку, которую нужно проанализировать, 
и букву, частоту повторения которой нужно найти. 
В качестве ответа верните одно число — количество повторений буквы в строке.
'''
# def count_letters(str_, substr_):
#     result = 0
#
#     for i in str_.lower():
#         if i == substr_:
#             result +=1
#
#     return result
#
#
# print(count_letters('KabshanovK', 'k'))

'''
Напишите функцию decipher(), которая заменит все числа в строке на буквы русского алфавита. 
Функция должна принимать один аргумент — строку с целыми числами от 0 до 32, между которыми стоит пробел. 
В качестве ответа верните строку с последовательностью букв без пробелов и других разделителей. 
Используйте только строчные буквы.
'''
# def decipher(string_number):
#     russian_letters = [
#         'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
#         'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
#         'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
#     ]
#     string_number_list = string_number.split(' ')
#     decrypted_text = []
#     for number in string_number_list:
#         letter_number = int(number)
#         letter = russian_letters[letter_number]
#         decrypted_text.append(letter)
#
#
#     return ''.join(decrypted_text)
#
#
# a = '0 1 2'
#
# print(decipher(a))

'''
Создайте функцию all_dividers(), которая найдет все делители числа. 
Она должна принимать на вход один аргумент — число, которое нужно разложить на множители. 
В качестве ответа верните список со всеми делителями исходного числа.
'''

def all_dividers(number):
    list_number = []
    for i in range(1, number+1):
        if number % i == 0:
            list_number.append(i)

    return list_number

print(all_dividers(12))