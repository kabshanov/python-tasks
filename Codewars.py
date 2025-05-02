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
'''
'world'  =>  'dlrow'
'word'   =>  'drow'
'''
# def solution(string:str):
#     print(''.join(list(reversed(string))))
#     print(string[::-1])
#
# solution('abc')
'''
В этом простом задании вам дано число, которое нужно сделать отрицательным. Но, может быть, число уже отрицательное?

Примеры
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
Примечания
Это число уже может быть отрицательным, и в этом случае никаких изменений не требуется.
Ноль (0) не проверяется на наличие какого-либо конкретного знака. Отрицательные нули не имеют математического смысла.
'''
# def make_negative(i):
#     # if number > 0:
#     #     result = number * -1
#     #     return result
#     # else:
#     #     return number
#     return i * -1 if i > 0 else i
#
# print(make_negative(10))
'''
Задача
Вы получаете массив чисел и возвращаете сумму всех положительных чисел.

Пример
[1, -4, 7, 12] => 
1
+
7
+
12
=
20
1+7+12=20
Примечание
Если суммировать нечего, сумма по умолчанию равна 0.
'''
# def positive_sum(b):
#     return sum([a for a in b if a > 0])
#
# print(positive_sum([1,-2,3,4,5]))

'''
Это довольно просто. Ваша задача — создать функцию, которая удаляет первый и последний символы строки. 
Вам даётся один параметр — исходная строка. Вам не нужно беспокоиться о строках, в которых меньше двух символов.
'''
# # мое решение
# def remove_char(s):
#     return s[1:-1]
#
# print(remove_char('place'))

'''
Дополните функцию вычисления суммы квадратов так, чтобы она возводила в квадрат каждое переданное ей число, а затем суммировала результаты.

Например, для [1, 2, 2] он должен вернуть 9, потому что 
'''
# def absurd_min(nums):
#     s=''.join(str(i)+' ' for i in nums).rstrip()
#     arr,tmp,sgn=[],0,1
#     for ch in s:
#         ((ch=='-') and (sgn:=-1)) or ((ch>'/') and (tmp:=tmp*10+(ord(ch)&15))) or (arr.append(sgn*tmp),tmp:=0,sgn:=1)
#     arr.append(sgn*tmp)
#     Y=lambda f:(lambda x:f(lambda *a:x(x)(*a)))(lambda x:f(lambda *a:x(x)(*a)))
#     return Y(lambda r:lambda seq,m=None,i=0:m if i==len(seq) else r(seq,seq[i] if (m is None or seq[i]<m) else m,i+1))(tuple(arr))
'''
Напишите функцию, которая удаляет пробелы из строки, а затем возвращает полученную строку.

Примеры (Ввод -> Вывод):

"8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
"8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
"8aaaaa dddd r     " -> "8aaaaaddddr"
'''
# def no_space(x):
#     return x.replace(' ', '')
#
# print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))

# def are_you_playing_banjo(name):
#     # Implement me!
#     return name + " plays banjo" if name[0] == 'r' or name[0] == 'R' else name + " does not play banjo"
#
# print(are_you_playing_banjo('martin'))
'''
Учитывая две строки, состоящие из + и -, верните новую строку, которая показывает, как эти две строки взаимодействуют следующим образом:

Когда позитив и положительные стороны взаимодействуют, они остаются позитивными.
Когда негативы взаимодействуют, они остаются негативными.
Но когда отрицательные и положительные заряды взаимодействуют, они становятся нейтральными и отображаются в виде числа 0.
Отработанный Пример
("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
Примеры
("--++--", "++--++") ➞ "000000"

("-+-+-+", "-+-+-+") ➞ "-+-+-+"

("-++-", "-+-+") ➞ "-+00"
'''
# мое решение
# def neutralise(s1: str, s2: str):
#     result = []
#     for i, _s1 in enumerate(s1):
#         if _s1 == '-' and s2[i] =='-':
#             result.append('-')
#         elif _s1 == '+' and s2[i] =='+':
#             result.append('+')
#         elif _s1 == '-' and s2[i] =='+':
#             result.append('0')
#         else:
#             result.append('0')
#     return ''.join(result)
#
# print(neutralise("-+-+-+", "-+-+-+"))
'''
Наша футбольная команда завершила чемпионат.

Результаты матчей нашей команды записываются в виде набора строк. 
Каждый матч представлен строкой в формате "x:y", где x — счёт нашей команды, а y — счёт соперника.

Например: ["3:1", "2:2", "0:1", ...]

Очки начисляются за каждый матч следующим образом:

если x > y: 3 очка (победа)
если x < y: 0 очков (проигрыш)
если x = y: 1 очко (ничья)
Нам нужно написать функцию, которая принимает этот набор данных и возвращает количество очков, 
набранных нашей командой (x) в чемпионате по приведённым выше правилам.

Примечания:

наша команда всегда проводит 10 матчей в чемпионате
0 <= x <= 4
0 <= y <= 4
'''
# мое решение
# def points(games):
#     result = []
#
#     for game in games:
#         x = game[0]
#         y = game[2]
#         if x > y:
#             result.append(3)
#         elif x < y:
#             result.append(0)
#         else:
#             result.append(1)
#
#     sum_result = sum(result)
#
#     return sum_result
#
# print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
'''
Если ты не можешь заснуть, просто посчитай овец!!

Задача:
Например, если дано неотрицательное целое число 3, верните строку с бормотанием: "1 sheep...2 sheep...3 sheep...". 
Ввод всегда будет корректным, то есть без отрицательных целых чисел.
'''
# def count_sheep(n):
#     result = []
#     for i in range(1, n+1):
#         result.append(f'{i} sheep...')
#     return ''.join(result)
#
# print(count_sheep(3))
'''
Дополните решение так, чтобы оно возвращало true, 
если первый переданный аргумент (строка) заканчивается вторым аргументом (тоже строкой).

Примеры:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''
# def solution(text, ending):
#     return text.endswith(ending)
#
#
#
# print(solution('abc', 'd'))
'''
Create a function add(n)/Add(n) which returns a function that always adds n to any number

Note for Java: the return type and methods have not been provided to make it a bit more challenging.

add_one = add(1)
add_one(3)  # 4

add_three = add(3)
add_three(3) # 6
'''
# def add(n):
#     def inner(x):
#         return x + n
#     return inner
#
# add_one = add(1)  # теперь add_one — функция, которая делает x + 1
# print(add_one(3))        # → 3 + 1 = 4
'''
Напишите функцию factory, которая принимает число в качестве параметра и возвращает другую функцию.

Возвращаемая функция должна принимать в качестве параметра массив чисел и возвращать массив этих чисел, 
умноженных на число, переданное в первую функцию.

В приведённом ниже примере 5 — это число, переданное в первую функцию. 
Таким образом, она возвращает функцию, которая принимает массив и умножает все его элементы на пять.

Переводы и комментарии (и положительные отзывы) приветствуются!

Пример
fives = factory(5)          # returns a function - fives
my_array = [1, 2, 3]
fives(my_array)             # returns [5, 10, 15]
'''
# # def factory(x):
# #     def inner(lst):
# #         return [el * x for el in lst]
# #     return inner
# def factory(x):
#     return lambda lst: [el * x for el in lst]
#
#
#
# fives = factory(5)          # returns a function - fives
# my_array = [1, 2, 3]
# print(fives(my_array))       # returns [5, 10, 15]
'''
Для заданного списка цифр 0 до 9 верните список с теми же цифрами в том же порядке, но со всеми 0 в паре. 
При соединении двух 0 получается один 0 на месте первого.

Примеры
input: [0, 1, 0, 2]
paired: ^-----^
    -> [0, 1,   2]
  kept: ^

input: [0, 1, 0, 0]
paired: ^-----^
    -> [0, 1,    0]
  kept: ^        ^

input: [1, 0, 7, 0, 1]
paired:    ^-----^
    -> [1, 0, 7,    1]
  kept:    ^

input: [0, 1, 7, 0, 2, 2, 0, 0, 1, 0]
paired: ^--------^        ^--^
    -> [0, 1, 7,    2, 2, 0,    1, 0]
  kept: ^                 ^        ^
Примечания
Соединение происходит слева направо. При каждом соединении второе 0 всегда будет соединено с первым (справа налево)
0сгенерированные в результате сопряжения файлы не могут быть сопряжены повторно
(если не применимо: ) не изменяйте входной массив, иначе вы не пройдете тесты
'''
# def pair_zeros(arr):
#     result = []
#     count = 0
#     for el in arr:
#         if el == 0:
#             if count % 2 == 0:
#                 result.append(el)
#                 count += 1
#             else:
#                 count += 1
#         else:
#             result.append(el)
#     return result
#
# print(pair_zeros([0, 0, 0]))
'''
Чтобы выполнить это задание, вам нужно создать функцию multiplyAll/multiply_all, 
которая принимает в качестве аргумента массив целых чисел. 
Эта функция должна возвращать другую функцию, 
которая принимает в качестве аргумента одно целое число и возвращает новый массив.

Возвращаемый массив должен состоять из каждого элемента первого массива, умноженного на целое число.

Пример:

multiply_all([1, 2, 3])(2); // => [2, 4, 6]
Вы не должны изменять исходный массив.
'''
# def multiplyAll(lst):
#     return lambda n: [el * n for el in lst]
#
# lst = multiplyAll([1, 2, 3])
# print(lst(2))
'''
Вам будет предоставлен массив объектов (ассоциативных массивов в PHP), представляющих данные о разработчиках, 
которые зарегистрировались для участия в следующем собрании программистов, которое вы организуете. 
Список упорядочен в соответствии с тем, кто зарегистрировался первым.

Ваша задача - вернуть одну из следующих строк:

< firstName here >, < country here > первого разработчика Python, который зарегистрировался; или
There will be no Python developers если ни один разработчик Python не зарегистрировался.
Например, учитывая следующий входной массив:

list1 = [
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
]
ваша функция должна вернуть значение Victoria, Puerto Rico.
'''
# def get_first_python(users):
#     for user in users:
#         if user.get('language') == 'Python':
#             return f"{user.get('first_name')}, {user.get('country')}"
#     return 'There will be no Python developers'
#
# list1 = [
#   { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
#   { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
#   { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
# ]
#
# print(get_first_python(list1))
'''
Напишите функцию, которая возвращает последовательность (индекс начинается с 1) всех чётных символов из строки. 
Если длина строки меньше двух символов или больше 100 символов, функция должна возвращать «некорректную строку».

Например:

"abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
"a"             --> "invalid string"
'''
def even_chars(st):
    result = []
    count = 1
    for el in range(len(st)+1):
        if len(st) < 2 or len(st) > 100:
            return 'invalid string'
        else:
            if el == st[0]:
                continue
            else:
                result.append(count)
                count += 2

    return result

print(even_chars("abcdefghijklm"))




#https://www.codewars.com/kata/583ea278c68d96a5fd000abd
