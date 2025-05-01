'''
Напишите функцию, которая принимает на вход строку и выводит результаты в соответствии со следующей таблицей:

Входные данные	Выходной сигнал
"Джаброни"	"Текила Патрона"
"Школьный консультант"	"Что-нибудь с алкоголем"
"Программист"	"Хипстерское Крафтовое пиво"
"Член Велосипедной банды"	"Самогон"
"Политик"	"Ваши налоговые доллары"
"Рэпер"	"Кристалл"
что - нибудь еще	"Пиво"
любое другое значение Примечание: — это значение по умолчанию:
если на вход функции не поступает ни одно из значений из таблицы,
то возвращаемое значение должно быть "Beer".

Убедитесь, что вы учитываете случаи, когда некоторые слова отображаются без правильной прописной буквы.
Например, ввод "pOLitiCIaN" по-прежнему должен возвращать "Your tax dollars".

'''
from importlib.metadata import pass_none

# drink_by_profession = {
#     "Jabroni": "Patron Tequila",
#     "School Counselor": "Anything with Alcohol",
#     "Programmer": "Hipster Craft Beer",
#     "Bike Gang Member": "Moonshine",
#     "Politician": "Your tax dollars",
#     "Rapper": "Cristal"
# }
#
# def get_drink_by_profession(msg):
#     return drink_by_profession.get(msg.title(), 'Beer')


'''
Ваш коллега написал простой цикл для вывода списка его любимых животных. 
Но, похоже, в грамматике есть небольшая ошибка, из-за которой программа не работает. Исправьте её! :)

Если вы передадите в функцию список своих любимых животных, 
вы должны получить список животных с упорядоченными названиями и добавленными новыми строками.

Например, передавая в:

[ "dog", "cat", "elephant" ]
приведет к:

"1. dog\n2. cat\n3. elephant\n"

Это как я понял>
1. dog
2. cat
3. elephant
'''
# def foo(animals):
#     result = ""
#     for i, element in enumerate(animals, start=1):
#         result += f"{i}. {element}\n"
#     return result
#
# text = ["dog", "cat", "elephant"]
# print(foo(text))
#
# #или
# def list_animals(animals):
#     lst = ''
#     for i in range(len(animals)):
#         lst += str(i + 1) + '. ' + animals[i] + '\n'
#     return lst

'''
Описание:
Уберите все восклицательные знаки в конце предложения.

Примеры
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"
'''
# def remove(st:str) :
#     return st.rstrip('!')
#
# text = "Hi!!! Hi! Hi!"
#
# print(remove(text))

'''
Создайте функцию finalGrade, которая вычисляет итоговую оценку учащегося в зависимости от двух параметров: 
оценки за экзамен и количества выполненных проектов.

Эта функция должна принимать два аргумента: экзамен — оценка за экзамен (от 0 до 100); 
проекты — количество выполненных проектов (от 0 и выше);

Эта функция должна возвращать число (окончательную оценку). Существует четыре типа окончательных оценок:

100 баллов, если оценка за экзамен выше 90 или если количество выполненных проектов превышает 10.
90 баллов, если оценка за экзамен выше 75 баллов и если количество выполненных проектов не менее 5.
75 баллов, если оценка за экзамен превышает 50 баллов и если количество выполненных проектов составляет минимум 2.
0, в других случаях
Примеры(Входные данные-->Выходные данные):

100, 12 --> 100
99, 0 --> 100
10, 15 --> 100

85, 5 --> 90

55, 3 --> 75

55, 0 --> 0
20, 2 --> 0
'''
# def final_grade(exam, projects):
#     if exam > 90 or projects > 10:
#         return 100
#     elif exam > 75 and projects >= 5:
#         return 90
#     elif exam > 50 and projects >=2:
#         return 75
#     else:
#         return 0

'''
Возвращает количество гласных в заданной строке.

В этой ката мы будем считать гласные a, e, i, o, u (но не y).

Входная строка будет состоять только из строчных букв и / или пробелов.
'''
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# def get_count(sentence):
#     count_ = 0
#     for vowel in sentence:
#         if vowel in  vowels:
#             count_ +=1
#
#     return count_
#
# print(get_count("jjdaa"))

'''
Тролли атакуют ваш раздел комментариев!

Распространённый способ справиться с этой ситуацией — удалить из комментариев троллей все гласные, нейтрализовав угрозу.

Ваша задача — написать функцию, которая принимает строку и возвращает новую строку без гласных.

Например, строка «This website is for losers LOL!» превратится в «Ths wbst s fr lsrs LL!».

Примечание: в этом ката y не считается гласной.
'''
# def disemvowel(string_) :
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     list_ =[]
#
#     for char in string_:
#         if char not in vowels:
#             list_.append(char)
#
#     string_ = ''.join(list_)
#
#     return string_
#
# print(disemvowel("This website is for losers LOL!"))

'''
Добро пожаловать. В этой задаче вам нужно возвести в квадрат каждую цифру числа и объединить их.

Например, если мы пропустим 9119 через функцию, получится 811181, потому что 92 — это 81, а 12 — это 1. (81-1-1-81)

Пример № 2: при вводе 765 будет/должно получиться 493625, потому что 72 равно 49, 62 равно 36, а 52 равно 25. (49-36-25)

Примечание: Функция принимает целое число и возвращает целое число.

Счастливого Кодирования!
'''
# def square_digits(num: int):
#     digits = list(str(num))
#     result = ''
#
#     for n in digits:
#         n_int = int(n)
#         result += str(n_int ** 2)
#
#     return result
#
#
# print(square_digits(9119))

'''
В этом небольшом задании вам дана строка чисел, разделённых пробелами, и нужно вернуть самое большое и самое маленькое числа.

Примеры
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Примечания
Все номера действительны Int32, нет необходимости их подтверждать.
Во входной строке всегда будет хотя бы одно число.
В выходной строке должно быть два числа, разделённых одним пробелом, причём большее число должно стоять первым.
'''
#def high_and_low(numbers: str):
#     digits = numbers.split(' ')
#     digits_list = []
#
#     for num in digits:
#         num_int = int(num)
#         digits_list.append(num_int)
#
#     num_max = str(max(digits_list))
#     num_min = str(min(digits_list))
#
#     return f'{num_max} {num_min}'
#
#
# print(high_and_low("1 9 3 4 -5"))

'''
В этом задании вам нужно создать функцию, 
которая принимает список неотрицательных целых чисел 
и строк и возвращает новый список с отфильтрованными строками.

Пример
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
'''
# def filter_list(l):
#     number_list = []
#
#     for i in l:
#         if type(i) == int:
#             number_list.append(i)
#
#     return number_list
#
#
# print(filter_list([1,2,'aasf','1','123',123]))

'''
Ваша задача — создать функцию, которая может принимать в качестве аргумента 
любое неотрицательное целое число и возвращать его с цифрами в порядке убывания. 
По сути, нужно переставить цифры так, чтобы получилось максимально возможное число.

Примеры:
Ввод: 42145 Вывод: 54421
Ввод: 145263 Вывод: 654321
Ввод: 123456789 Вывод: 987654321
'''
# def descending_order(num):
#     return int(''.join(sorted([str(n) for n in str(num)], reverse=True)))
#
# print(descending_order(123456789))
'''
Ваша задача
Учитывая массив логических значений и логический оператор, верните логическое значение, последовательно применяя оператор к значениям в массиве.

Примеры
логические значения = [True, True, False], оператор = "AND"
True AND True -> True
True AND False -> False
Возврат False
логические значения = [True, True, False], оператор = "OR"
True OR True -> True
True OR False -> True
Возврат True
логические значения = [True, True, False], оператор = "XOR"
True XOR True -> False
False XOR False -> False
Возврат False
Входные данные
массив логических значений (1 <= array_length <= 50)
строка, задающая логический оператор: "AND", "OR", "XOR"
Выходной сигнал
Логическое значение (True или False).
'''
# def logical_calc(array, op):
#     result = array[0]
#     for value in array[1:]:
#         if op == "OR":
#             result = result or value
#         elif op == "AND":
#             result = result and value
#         elif op == "XOR":
#             result = result ^ value
#     return result
#
#
# print(logical_calc([True, False], "OR"))
'''
Завершите функцию uefaEuro2016(), чтобы она возвращала строку, как в приведённых ниже примерах:

uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."
'''
# def uefa_euro_2016(teams, scores):
#     if scores[0] > scores[1]:
#         return f'At match {teams[0]} - {teams[1]}, {teams[0]} won!'
#     elif scores[0] < scores[1]:
#         return f'At match {teams[0]} - {teams[1]}, {teams[1]} won!'
#     else:
#         return f'At match {teams[0]} - {teams[1]}, teams played draw.'

'''
Учитывая массив чисел, проверьте, являются ли какие-либо из них 
кодами символов для гласных в нижнем регистре (a, e, i, o, u).

Если это так, измените значение массива на строку с этой гласной.

Верните результирующий массив.
'''
# def is_vow(inp: list):
#     vowel_codes = {
#         97 : 'a',
#         101 : 'e',
#         105 : 'i',
#         111 : 'o',
#         117 : 'u'
#     }
#
#     for idx in range(len(inp)) :
#         if inp[idx] in vowel_codes :
#             inp[idx] = vowel_codes[inp[idx]]
#
#     return inp
#
# print(is_vow([97, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ]))

'''
На ежегодном семейном собрании принято узнавать возраст самого старшего и самого младшего членов семьи и вычислять разницу между ними.

Вам будет предоставлен массив с возрастом всех членов семьи в произвольном порядке. 
Возраст будет указан в целых числах, поэтому ребёнку в возрасте 5 месяцев будет присвоен «возраст» 0. 
Верните новый массив (кортеж в Python) с [самым маленьким возрастом, 
самым большим возрастом, разницей между самым маленьким и самым большим возрастом].
'''
# def difference_in_ages(ages):
#     sort_ages = sorted(ages)
#     min_age = min(sort_ages)
#     max_age = max(sort_ages)
#     difference = max_age - min_age
#     result = (min_age, max_age, difference)
#     return result
#
# print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))
'''
Это спин-офф моего первого ката.

Вам дана строка, содержащая последовательность символов, разделённых запятыми.

Напишите функцию, которая возвращает новую строку, содержащую те же последовательности символов, 
кроме первой и последней, но на этот раз разделённую пробелами.

Если входная строка пуста или удаление первого и последнего элементов приведёт к тому, 
что результирующая строка будет пустой, верните пустое значение (в приведённых ниже примерах представлено в виде универсального значения NULL).

Примеры
"1,2,3"      =>  "2"
"1,2,3,4"    =>  "2 3"
"1,2,3,4,5"  =>  "2 3 4"

""     =>  NULL
"1"    =>  NULL
"1,2"  =>  NULL
'''
# def array(string: str):
#     string_list = string.split(',')
#     if len(string_list) < 3:
#         return None
#     else:
#         return ' '.join(string_list[1:-1])
#
# print(array("1,2,3,4,5"))

'''
Определите функцию, которая удаляет дубликаты из массива неотрицательных чисел и возвращает его в качестве результата.

Порядок следования должен оставаться прежним.

Примеры:

Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3]
'''
# def distinct(seq):
#     set_seq = set()
#     result = []
#     for item in seq:
#         if item not in set_seq:
#             set_seq.add(item)
#             result.append(item)
#     return result

'''
Получаем значение символа в формате ASCII.

С таблицей ASCII можно ознакомиться на http://www.asciitable.com/
'''
# def get_ascii(ch: str) -> int :
#     return ord(ch)
#
# print(get_ascii('\n'))

'''
Каждому начинающему хакеру нужен псевдоним! The Phantom Phreak, Acid Burn, Zero Cool и Crash Override — вот несколько ярких примеров из фильма Hackers.

Ваша задача — создать функцию, которая по имени и фамилии пользователя вернёт правильный псевдоним.

Примечания:
Два объекта, которые возвращают имя, состоящее из одного слова, в ответ на первую букву имени, 
и один объект, возвращающий имя, состоящее из одного слова, в ответ на первую букву фамилии, уже заданы. 
Дополнительные сведения см. в примерах ниже.

Если первый символ любого из имён, переданных функции, не является буквой из A - Z, 
вы должны вернуть "Your name must start with a letter from A - Z."

Иногда люди могут забывать писать первую букву своего имени с заглавной, 
поэтому ваша функция должна учитывать эти грамматические ошибки.

Примеры
# These two dictionaries are preloaded, you need to use them in your code
FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}

alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'
'''
# def alias_gen(f_name: str, l_name: str):
#     FIRST_NAME = {
#         'A' : 'Alpha',
#         'B' : 'Beta',
#         'C' : 'Cache',
#         'D' : 'Data',
#         'E' : 'Echo',
#         'F' : 'Function',
#         'G' : 'Glitch',
#         'H' : 'Half-Life',
#         'I' : 'Ice',
#         'J' : 'Java',
#         'K' : 'Keystroke',
#         'L' : 'Logic',
#         'M' : 'Malware',
#         'N' : 'Nagware',
#         'O' : 'OS',
#         'P' : 'Phishing',
#         'Q' : 'Quantum',
#         'R' : 'Radical',
#         'S' : 'Strike',
#         'T' : 'Trojan',
#         'U' : 'Ultraviolet',
#         'V' : 'Vanilla',
#         'W' : 'WiFi',
#         'X' : 'Xerox',
#         'Y' : 'Y',
#         'Z' : 'Zero'
#     }
#     SURNAME = {
#         'A' : 'Analogue',
#         'B' : 'Bomb',
#         'C' : 'Catalyst',
#         'D' : 'Discharge',
#         'E' : 'Electron',
#         'F' : 'Faraday',
#         'G' : 'Gig',
#         'H' : 'Hacker',
#         'I' : 'IP',
#         'J' : 'Jabber',
#         'K' : 'Kernel',
#         'L' : 'Link',
#         'M' : 'MitM',
#         'N' : 'Nuke',
#         'O' : 'Overclock',
#         'P' : 'Payload',
#         'Q' : 'Quark',
#         'R' : 'Router',
#         'S' : 'Spy',
#         'T' : 'T-Rex',
#         'U' : 'Unit',
#         'V' : 'Virus',
#         'W' : 'Worm',
#         'X' : 'Xploit',
#         'Y' : 'Yob',
#         'Z' : 'Zombie'
#     }
#
#     letter_f_name = f_name[0].isalpha()
#     letter_l_name = l_name[0].isalpha()
#     # up_f_name = f_name[0] == f_name[0].upper()
#     # up_l_name = l_name[0] == l_name[0].upper()
#
#     is_valid = letter_f_name and letter_l_name
#
#     if is_valid:
#         first_name_alias = FIRST_NAME.get(f_name[0].upper())
#         last_name_alias = SURNAME.get(l_name[0].upper())
#         return f'{first_name_alias} {last_name_alias}'
#
#     else:
#         return f'Your name must start with a letter from A - Z.'
#
# print(alias_gen('123abc', 'Petrovic'))

'''
Вы идёте с сыном в лес, чтобы посмотреть на обезьян. Вы знаете, что их там определённое количество (n), 
но ваш сын слишком мал, чтобы просто оценить их количество, ему нужно начать считать их с 1.

Как хороший родитель, вы будете сидеть и считать вместе с ним. Учитывая число (n), 
заполните массив всеми числами до этого числа включительно, но без нуля.

Например(Ввод -> Вывод):

10 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 1 --> [1]
'''
# def monkey_count(n):
#     return [i+1 for i in range(n)]
#
#
# print(monkey_count(10))
'''
Вы — программист в SEO-компании. SEO-специалист вашей компании каждый день получает список всех ключевых слов проекта, 
а затем ищет самые длинные ключевые слова для их анализа.

Вы получите список ключевых слов и должны будете написать простую функцию, 
которая возвращает самые популярные ключевые слова и сортирует их в лексикографическом порядке.

Например, вы могли бы получить:

'key1', 'key2', 'key3', 'key n', 'bigkey2', 'bigkey1'
И ваша функция должна вернуть:

"'bigkey1', 'bigkey2'"
'''
#
#
# def the_biggest_search_keys(*args) :
#     if not args :
#         return "''"
#
#     count_list = {word : len(word) for word in args}
#     max_count = max(count_list.values())
#
#     candidates = []
#     for word in count_list :
#         if count_list[word] == max_count :
#             candidates.append(word)
#
#     sorted_candidates = sorted(candidates)
#
#     return ", ".join(f"'{word}'" for word in sorted_candidates)
#
#
# print(the_biggest_search_keys('key1', 'key2', 'key3', 'key n', 'bigkey2', 'bigkey1'))
'''
Натан любит кататься на велосипеде.

Поскольку Натан знает, что важно поддерживать водный баланс, он выпивает 0,5 литра воды за час езды на велосипеде.

Вам дано время в часах, и вам нужно вычислить количество литров, которое выпьет Натан, округлив в меньшую сторону.

Например:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
'''
# def litres(time):
#     return int(time * 0.5)
'''
Дано число n. Нарисуйте лестницу, используя букву "I". Лестница должна быть n в высоту и n в ширину, причём самая высокая ступенька должна находиться в левом верхнем углу.

Например , n = 3 приведет к:

"I\n I\n  I"
или напечатанный:

I
 I
  I
Другой пример, лестница из 7 ступеней должна быть нарисована следующим образом:

I
 I
  I
   I
    I
     I
      I
'''
# def draw_stairs(n):
#     result = []
#     for i in range(n):
#         result.append(' ' * i + 'I')
#     return '\n'.join(result)
'''
Компания, в которой вы работаете, только что получила контракт на создание платёжного шлюза. Чтобы ускорить процесс, вы вызвались создать функцию, которая будет принимать число с плавающей точкой и возвращать сумму в долларах и центах.

39.99 becomes $39.99

Остальные члены вашей команды позаботятся о том, чтобы аргумент был очищен перед передачей в вашу функцию, хотя вам нужно будет учитывать добавление конечных нулей, если они отсутствуют (хотя вам не придётся беспокоиться о пропущенном периоде).

Примеры:

3 needs to become $3.00

3.1 needs to become $3.10
'''
# def format_money(amount):
#     return f'${amount}' if amount == float else f"${amount:.2f}"
'''
Вы должны создать функцию spread, которая принимает функцию и список аргументов, которые будут применяться к этой функции. 
Вы должны сделать так, чтобы эта функция возвращала результат вызова заданной функции/лямбда-выражения с заданными аргументами.

например:

spread(someFunction, [1, true, "Foo", "bar"] ) 
# is the same as...
someFunction(1, true, "Foo", "bar")
'''
# def spread(func, args):
#     return func(*args)
#
# def someFunction(a, b, c, d):
#     return f"{a}, {b}, {c}, {d}"

# print(spread(someFunction, [1, True, "Foo", "bar"]))
'''
Напишите функцию unpack(), которая распаковывает list элементов, 
которые могут содержать объекты(int, str, list, tuple, dict, set) внутри друг друга 
без какой-либо заранее заданной глубины, то есть элементы могут находиться на разных уровнях.

Пример:

unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]) == [None, 1, 2, 3, 'foo', 'bar']
Примечание: вам не нужно беспокоиться о порядке элементов, 
особенно при распаковке dict или set. Просто распакуйте все элементы.
'''
# def unpack(lst):
#     result = []
#     for item in lst:
#         if isinstance(item, (list, tuple, set)):
#             result.extend(unpack(item))  # рекурсия для list/tuple/set
#         elif isinstance(item, dict):
#             # Рекурсивно распаковываем и ключи, и значения
#             result.extend(unpack(item.keys()))
#             result.extend(unpack(item.values()))
#         else:
#             result.append(item)
#     return result
#
#
# print(unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]))
'''
Создайте функцию под названием _if с тремя аргументами: значением bool и двумя функциями (без параметров): func1 и func2

Если bool истинно, то следует вызвать func1, в противном случае вызовите func2.

Пример:
def truthy(): 
  print("True")
  
def falsey(): 
  print("False")
  
_if(True, truthy, falsey)
# prints 'True' to the console
'''
# def truthy() :
#     print("True")
#
#
# def falsey() :
#     print("False")
#
#
# def _if(bool, func1, func2) :
#     return func1() if bool else func2()
#
#
# _if(True, truthy, falsey)
'''
Напишите функцию с именем numbers.

Функция должна возвращать True, 
если все переданные ей параметры являются целыми числами 
или числами с плавающей точкой. 
В противном случае функция должна возвращать False.

Функция должна принимать любое количество параметров.

Пример использования:

numbers(1, 4, 3, 2, 5); # True
numbers(1, "a", 3); # False
numbers(1, 3, None); # False
numbers(1.23, 5.6, 3.2) # True
'''
def numbers(*args):
    for item in args:
        if not isinstance(item, (int, float)):
            return False
    return True

print(numbers((1, 4, 3, 2, 5)))































