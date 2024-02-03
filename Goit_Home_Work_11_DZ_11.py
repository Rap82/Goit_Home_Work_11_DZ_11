# ============================== Модуль 11 / Modul 11 =============================================

# +++++++++++++++++++++++++++++  'Магічні' методи  ++++++++++++++++++++++++++++++++++++++

#                     1.'Магічні' методи
#                     2. Метод init
#                     3. Методи str та repr
#                     4. Методи getitem та setitem
#                     5. Функтори, метод call
#                     6. Створення власних менеджерів контексту
#                     7. Створення об'єкта ітератора/генератора
#                     8. Інкапсуляція у Python (property, setter).
#                     9. Перевизначення математичних операторів
#                     10. Перевизначення операцій порівняння


# ================================ Звдання 1 / Task 1 ======================================

# ================================  Метод init  ==========================

# Найчастіше використовуваний магічний метод — це метод __init__. Цей метод відповідає за ініціалізацію об'єкта. 
# Коли ви створюєте об'єкт класу, спочатку створюється порожній об'єкт, який містить лише обов'язкові службові атрибути. 
# Після цього (об'єкт вже створено) автоматично викликається метод __init__, який ви можете модифікувати під ваші потреби.

# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         return f'Hello! I am {self.name}'


# bill = Human('Bill')
# print(bill.say_hello())  # Hello! I am Bill
# print(bill.age)  # 0

# jill = Human('Jill', 20)
# print(jill.say_hello())  # Hello! I am Jill
# print(jill.age)  # 20
# В цьому прикладі ми створили клас Human, у якому визначили метод __init__. 
# У цьому методі ми додаємо об'єктам цього класу поля name та age. Зверніть увагу, 
# що метод __init__ може приймати аргументи позиційні і/або іменні, як будь-який інший метод. 
# Коли ми створюємо об'єкт класу Human, ми повинні класу передати обов'язково хоч один аргумент, 
# скільки метод __init__ повинен приймати обов'язково name.

# __init__ не обов'язково приймає аргументи та містить лише створення полів. 
# Цей метод можна використовувати для реалізації будь-яких дій, які вам потрібні на етапі, 
# коли об'єкт вже створено та його треба ініціалізувати.

# ++++++++++++++++++++++++++++++++++++++Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Створіть клас Point, який відповідатиме за відображення геометричної точки на площині.

# Реалізуйте через конструктор __init__ ініціалізацію двох атрибутів: координати x та координати y.

# Приклад:

# point = Point(5, 10)

# print(point.x)  # 5
# print(point.y)  # 10

# ++++++++++++++++++++ Код / Code ++++++++++++++++++++++++++++++++++++

# class Point: # Створення класу Point
#     '''Реалізація класу , Клас містить два обовязкових аргументи і поля 
#     Перше поле *.x  з одноіменим аргументом *x ,
#     Друге поле *.y з одноіменим аргументом *y '''
#     def __init__(self, some_x, some_y) -> None: 
#         '''Конструктор класу , вньому описуємо/ралізуємо обовязкові власні поля і значення які вони мають набути'''

#         self.x = some_x # Опис/реалізація поля *.x для екзеплярів цього класу .*class Point , 
#                    # При створені екземпляр , набуває значення передане як перший обовязковий аргумент *some_x # Шаблон екзепляру Point(*x, *y) 
#         self.y = some_y # Опис/реалізація поля *.y для екзеплярів цього класу .*class Point , 
#                    # При створені екземпляр , набуває значення передане як другий обовязковий аргумент *some_y# Шаблон екзепляру Point(*x, *y)
        


# # +++++++++++++++++++++++++++++++++++++++++++ Тестові значення і виклик функції (не потрібний для автоперевірки.) ++++++++++++++++++++++

# point = Point(5, 10) # Стверення  екзепляру *point клас *class Point, з заданими початковими даними полів  *x і *y цього класу .
# point_1 = Point(5, 10) # Стверення  екзепляру *point_1 клас *class Point, з заданими початковими даними полів  *x і *y цього класу .
# some_name = Point("Стрічка", "Нічого собі .)") # і це також .), стверення  екзепляру *some_name клас *class Point, з заданими початковими даними полів  *x і *y цього класу .

# print(point)    # Ствоерений екзкпляр має вигляд *<__main__.Point object at 0x000001F8F57FA8D0>
# print(point.x)  # 5   # конкретне значення в полі *x цього екзкпляру.
# print(point.y)  # 10  # конкретне значення в полі *y цього екзкпляру.
# point.x = 100   # встановлення нового значення поля *x цього екзкпляру. (в тілі коду , не реалізації)
# print(point.x) # 100 # Принтим поле *x, перевіряємо чи змінилось значення. 
# print(point.y) # 10  # Принтим поле *y, перевіряємо чи змінилось значення.(поки поле *y не міняли тому значення є те що пристворенні екзепляру) 
# point.y = -45   # встановлення нового значення поля *y цього екзкпляру. 
# print(point.y) # -45 # Принтим поле *y, перевіряємо чи змінилось значення.( поле *y змінило своє початкове значення.)
# # ==============================
# print(point_1)    # Ствоерений екзкпляр має вигляд *<__main__.Point object at 0x000002AD371EA9C0>
# print(point_1.x)  # 50
# print(point_1.y)  # -10

# # =================================
# print(some_name)   # Ствоерений екзкпляр має вигляд *<__main__.Point object at 0x0000024B63ADA990>
# print(some_name.x) # Стрічка
# print(some_name.y) # Нічого собі .)


# ================================ Звдання 2 / Task 2 ======================================

# ================================  Прихвані поля , декоратори класів (@property, @імя_поля.setter) ==========================

# У Python неможливо інкапсулювати (зробити недоступними) атрибути класу. 
# Ви завжди можете отримати доступ до будь-якого атрибуту. Щоб якось вказати розробнику, 
# що доступ до атрибуту безпосередньо небажаний, прийнято називати такі поля чи методи, 
# починаючи з одного нижнього підкреслення. Якщо ж назвати атрибут так, що спочатку буде два нижні підкреслення, 
# то включиться механізм "приховання" імен. Це не означає, що доступ до цього поля буде закрито, просто небагато ускладнений.

# class Secret:
#     public_field = 'this is public'
#     _private_field = 'avoid using this please'
#     __real_secret = 'I am hidden'


# s = Secret()
# print(s.public_field)  # this is public
# print(s._private_field)  # avoid using this please
# print(s._Secret__real_secret)  # I am hidden
# Як видно з цього прикладу, доступу за допомогою s.__real_secret ні, 
# але можна отримати доступ до цього ж поля через s._Secret__real_secret, що загалом нічого не захищає.

# Цей механізм можна використовувати для реалізації механізму setter та getter. 
# Буває, виникає необхідність перевірити, що користувач хоче записати в поле. 
# Для цього можна написати окремий метод, який буде перед збереженням значення в полі реалізовувати перевірку, 
# але саме поле, як і раніше, залишиться доступним. Можна ж скористатися декоратором setter. 
# Для обчислення значення "на льоту" або як пару для setter можна скористатися декоратором property, 
# який перетворює будь-який метод на поле. Наприклад, ми хочемо перевірити, що користувач вводить лише додатні числа.

# class PositiveNumber:
#     def __init__(self):
#         self.__value = None

#     @property
#     def value(self):
#         return self.__value

#     @value.setter
#     def value(self, new_value):
#         if new_value > 0:
#             self.__value = new_value
#         else:
#             print('Only numbers greater zero accepted')

# ++++++++++++++++++++++++++++++++++++++  Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# У класу Point через конструктор __init__ оголошено два атрибути: координати x та y. 
# Приховати доступ до них з допомогою подвійного підкреслення: __x та __y

# Реалізуйте для класу Point механізми setter та getter до атрибутів __x та __y за допомогою декораторів property та setter.

# Приклад:

# point = Point(5, 10)

# print(point.x)  # 5
# print(point.y)  # 10


# +++++++++++++++++++++++++++++++++++++   Код / Code ++++++++++++++++++++++++++++++++++++

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     @property # Вбудований декоратор класів. Утворює з будьякого методу до якого застосовано одноімене поле класу
#               # В нашому випадку, створить поле класу з іменем *x
#     def x(self):
#         ''' Метод без аргументів , повертає значення прихованого поля *__x , 
#         Така конструкція : Декоратор *@property і метод *x() дозволяє створити екзепляр класу , з можливістю
#          опрацювання даних переданих в поле ще до створення самого екзепляру.
#         Примітка: завдання просто застосувати самі декоратори без якогосось додаткового змісту і користі'''
#         return self.__x
   
    
#     @x.setter #'''Вбудований декоратор *@x.setter для методу/поля  *x. # повертає значення декоратору *@property
#     def x(self, new_x): 
#         '''Метод приймає один обовязковий аргументи.
#           і повертає його відповідному полю екзепляру класу
#         Примітка: завдання просто застосувати самі декоратори без якогосось додаткового змісту і користі'''
        
#         self.__x = new_x # Якщо додатнє присвоюємо його прихованій змінні/полю *self.__x
    
#     @property # Вбудований декоратор класів. Утворює з будьякого методу до якого застосовано одноімене поле класу
#               # В нашому випадку, створить поле класу з іменем *y
#     def y(self):
#         ''' Метод без аргументів , повертає значення прихованого поля  *__y 
#         Така конструкція : Декоратор *@property і метод *y() дозволяє створити екзепляр класу , з можливістю
#          опрацювання даних переданих в поле ще до створення самого екзепляру.
#         Примітка: завдання просто застосувати самі декоратори без якогосось додаткового змісту і користі'''
           
#         return self.__y
       
#     @y.setter # Вбудований декоратор *@y.setter для методу/поля  *y. # повертає значення декоратору *@property
#     def y(self, new_y): 
#         '''Метод приймає один обовязковий аргументи.
#           і повертає його відповідному полю екзепляру класу
#         Примітка: завдання просто застосувати самі декоратори без якогосось додаткового змісту і користі'''
#         self.__y = new_y # присвоюємо  прихованій змінні/полю *self.__y значення *new_y, 
#                          # в нашому випадку друге значення в круглих дужках для Шаблону екзепляру *Point(x, y) .
        

# # # +++++++++++++++++++++++++++++++++++++++++++ Тестові значення і виклик функції (не потрібний для автоперевірки.) ++++++++++++++++++++++

# point = Point(5, 10)

# print(point.x)  # 5
# print(point.y)  # 10

# ================================ Звдання 3 / Task 3 ======================================

# ================================  Прихвані поля , декоратори класів (@property, @імя_поля.setter) ==========================


# Розглянемо таку ситуацію. У нас є клас Person, який має властивість name

# class Person:
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         if (type(name) == str) and (len(name) > 0):
#             self.__name = name


# person = Person(123)
# print(person.name)  # 123
# У цьому коді може виникнути помилка. В setter ми робимо перевірку, 
# щоб значення було рядком та чекаємо тільки рядок ненульової довжини. 
# Але при ініціалізації значення в конструкторі, 
# коли привласнюємо self.__name=name ми насправді ігноруємо роботу setter та привласнюємо значення безпосередньо. 
# Що і сталося в нашому коді — властивість __name містить числове значення.

# Щоб цього не відбувалося, код треба переписати так:

# class Person:
#     def __init__(self, name):
#         self.__name = None
#         self.name = name

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         if (type(name) == str) and (len(name) > 0):
#             self.__name = name


# person = Person(123)
# print(person.name)  # None
# Зараз у конструкторі ми привласнюємо полю __name значення None: self.__name=None.
# У другому рядку конструктора ми примусово викликаємо setter інструкцією self.name=name. 
# У такому разі setter виконується і не дозволяє нам привласнити полю __name 
# не валідне значення 123 при створенні екземпляра класу person = Person(123).

# ++++++++++++++++++++++++++++++++++++++  Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# У класу Point до механізму setter властивостей x і y додайте перевірку на значення, що вводиться. 
# Дозвольте встановлювати значення властивостей x та y для екземпляра класу, 
# тільки якщо вони мають числове значення (int або float).

# Приклад:

# point = Point("a", 10)

# print(point.x)  # None
# print(point.y)  # 10


# +++++++++++++++++++++++++++++++++++++   Код / Code ++++++++++++++++++++++++++++++++++++

# Примітка : Завдання схоже на завдання 2 . Читай про приховані поля , декоратори  @property і @імя.setter в 2 завдані.
            # Відміність в тому що в конструкторі ми передаємо два аргументи *x, *y .
            # і щоб їх значення встановилось в екзепляр(якщо вони пройдуть перевірку @property і @імя.setter ) потрібно їх явно оголосити в конструкорі.
            # *self.x = x , *self.y = y - явно оголошення полів і їх значень в конструкторі.
            # Є умова що дані мають бути типу *int , *float
# class Point:
#     def __init__(self, x, y): # Конструктор, приймає два аргументи які будуть передані екзепляру після перевірки значень на віповідність умові.
#         self.__x = None # Приховане значення поля *х , Початкове знчення *None, 
#                         # Присвоється екзепляру якщо значення передані цьому полю не пройдуть перевірку *@property і *@імя.setter
#         self.__y = None # Приховане значення поля *y , Початкове знчення *None, 
#                         # Присвоється екзепляру якщо значення передані цьому полю не пройдуть перевірку *@property і *@імя.setter
#         self.x = x # Реалізація явного поля *x, буда встановленне відповідна значення з аргумента *x , якщо пройде перевірку *@property і *@імя.setter 
#         self.y = y # # Реалізація явного поля *y, буда встановленне відповідна значення з аргумента *y , якщо пройде перевірку *@property і *@імя.setter

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, new_x):
       
#         if type(new_x) == int or type(new_x) == float: # Перевіряємо чи передані дані в поле *x типу *int або *float

#             # isinstance(y,int) or isinstance(y, float) - такий запис не проходить атвтоперевірку 
#             # Примітка від ментора : Автоперевірка перевіряє ваш код з багатьма значеннями. І тут є проблема з isinstance.
#             # Оскільки він повертає True не тільки для типів, а ще і для типів, які наслідуються від типу.
#             # Оскільки bool наслідується від int, то isinstance(True,  int) буде True. 
#             # Більш детально ви можете прочитати ввівши help(True) у інтерпретаторі.
#             # А щоб уникнути цю помилку, потрібно скористатися функцією type, яка буде повертати конкретні типи:
#             # if type(new_x) == int
#             self.__x = new_x
#         else:
#             self.__x
        
            

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, new_y):
        
#         if type(new_y) == int or type(new_y) == float :  # Перевіряємо чи передані дані в поле *y типу *int або *float

#             # isinstance(y,int) or isinstance(y, float) - такий запис не проходить атвтоперевірку 
#             # Примітка від ментора : Автоперевірка перевіряє ваш код з багатьма значеннями. І тут є проблема з isinstance.
#             # Оскільки він повертає True не тільки для типів, а ще і для типів, які наслідуються від типу.
#             # Оскільки bool наслідується від int, то isinstance(True,  int) буде True. 
#             # Більш детально ви можете прочитати ввівши help(True) у інтерпретаторі.
#             # А щоб уникнути цю помилку, потрібно скористатися функцією type, яка буде повертати конкретні типи:
#             # if type(new_x) == int
            
#             self.__y = new_y
#         else:
#             self.__y



# # # # +++++++++++++++++++++++++++++++++++++++++++ Тестові значення і виклик функції (не потрібний для автоперевірки.) ++++++++++++++++++++++

# point = Point("a", 10)

# print(point.x)  # None
# print(point.y)  # 10


# ================================ Звдання 4 / Task 4 ======================================

# ================================  4. Методи getitem та setitem  ==========================

# Квадратні дужки дозволяють вам звертатися до елементів послідовності індексу або елементів словника по ключу. 
# Коли ви хочете отримати значення, використовуючи квадратні дужки, об'єкт викликається метод __getitem__. 
# Для запису значення з індексом або ключем викликається метод __setitem__. 
# Обидва цих метода приймають першим аргументом self. __getitem__ другим аргументом приймає індекс чи ключ, 
# яким треба знайти елемент, а __setitem__ другим аргументом приймає ключ/індекс, а третім значення, 
# яке треба записати за цим ключем/індексом.

# class ListedValuesDict:
#     def __init__(self):
#         self.data = {}

#     def __setitem__(self, key, value):
#         if key in self.data:
#             self.data[key].append(value)
#         else:
#             self.data[key] = [value]

#     def __getitem__(self, key):
#         result = str(self.data[key][0])
#         for value in self.data[key][1:]:
#             result += ", " + str(value)
#         return result


# l_dict = ListedValuesDict()
# l_dict[1] = 'a'
# l_dict[1] = 'b'
# print(l_dict[1])  # a, b

# У цьому прикладі ми створили власний клас, який веде себе як словник. 
# ListedValuesDict значення зберігає до списку і вже цей список зберігає як значення ключа. 
# Головна відмінність від словника у тому, що ListedValuesDict не дозволяє перезаписувати значення, 
# завжди додаватиме нове значення в кінець списку. І при отриманні значення повертає рядок, складений із значень у списку.


# ++++++++++++++++++++++++++++++++++++++  Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Реалізуйте клас Vector. Властивість coordinates визначає координати вектора і є екземпляром класу Point. 
# Нагадаємо, що вектором називають спрямований відрізок з початком та кінцем. 
# Початок у нас буде в точці (0, 0), а кінець вектора ми задаватимемо атрибутом coordinates.

# Реалізуйте можливість звертатися до координат екземпляра класу Vector через квадратні дужки:

# vector = Vector(Point(1, 10))

# print(vector.coordinates.x)  # 1
# print(vector.coordinates.y)  # 10

# vector[0] = 10  # Встановлюємо координату x вектора 10

# print(vector[0])  # 10
# print(vector[1])  # 10
# Щоб отримати значення, використовуючи квадратні дужки об'єкта print(vector[0]), реалізуйте метод __getitem__ у класу Vector.

# Для запису значення координат вектора через індекс, як vector[0] = 10, реалізуйте метод __setitem__ у класу Vector.

# Звернення до координати x проводиться за індексом 0, а звернення до координати y - за індексом 1.

# +++++++++++++++++++++++++++++++++++++   Код / Code ++++++++++++++++++++++++++++++++++++

# Примітка : *class_Point - реалізований аналогічно 3 завданню. Опис реалізаці дивись 3 завдання.
#            Опишу тільки клас *class_Vector  оскільки тут будемо використовувати нові магічні методи *__getitem__(self) і *__setitem__(self)

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y
    


# class Vector:
#     ''' Клас *Vector , має свій конструктор в якому реалізується поле *coordinates
#       приймає однин аргумент coordinates(очікується що буде предано екзепляр класу *Point(x,y) .
#       ###Робимо перевірку на тип , якщо тип даних переданий класу не *Point буде видавати принт (дивись в реалізацію конструктора який)
#       *Примітка: Перевірка на відповідність вхідних даних в завданні не потрібна(це для того щоб невикидало системної помилки в нашому коді коли спробуємо передати не той тип даних який описаний в умові як обвязковий)
#        за допомогою магічних методів *__getitem__ і *__setitem__ 
#        Метод *__getitem__(self, key) - створює можливість звертатись і повертати значення з екзепляру класу де реалізований , 
#                     за умовним індексом/ключем якщо передане значення в клас ітерабельне (інший екзеляр з більш ніж одним полем, або список або словник чи будь який інший обєект що містить кілька значень)
#                     Дозволені індекси передаються через значення *key, якщо в *key вказати значення яке не реалізоване в методі, то повертає ноне чи якийсь результт якщо ми це реалізуємо в метді
#                     (до прикладу принт з повідомлення, чи яку схочемо помилку за допомогою оператора *raise)
#                 # *Шаблон для нашого випадку: *vector = Vector(Point(1, 10)). Звернення буде наступне *vecor[0] == 1 і *vecor[1] == 10 (Ті значеня що передав екзепляр *Point(1, 10) відповідно) .
#                 При всіх інших звернення *vecor[3] чи *vecor[100] буде повертати *None , оскільки , в нашому випадку, є реалізовано коректні значення тільки для ключів 0 і 1 
#                 Ось ця реалізація  : *if index == 0: return self.coordinates.x , *if index == 1: return self.coordinates.y ,
#                                      де *if index == 0: return self.coordinates.x - якщо *key(в нашому випадку має назву *index  ) дорівнює 0 (*vecor[0]) поверни значення з поля *x яке є в екзеплярі *coordinates класу *Point
#                                         *if index == 1: return self.coordinates.y - якщо *key(в нашому випадку має назву *index  ) дорівнює 0 (*vecor[1]) поверни значення з поля *y яке є в екзеплярі *coordinates класу Point
        
#         Метод *__setitem__(self, index, value) - дозволяє встановлювати нові значення для цих полів, при зверненні з відповідни ключем.
                  
#                 # *Шаблон для нашого випадку: *vector = Vector(Point(1, 10)). Переприсвоєння буде наступне *vecor[0] = 11 і *vecor[1] = 15 (Принти *vecor[0] і *vecor[1] - будуть повертати вже новіз значення 11 і 15 відповідно ) .'''
    
#     
#     def __init__(self, coordinates: Point): # Коструктор класу , один аргумент (очікуєься екзепляр класу *Point вигляду *Point(x,y) )
#                                             # І стоврю одне власне одноєменне поле *self.coordinates, яке буде містити в значеннях цей екзепляр.
        
#         if type(coordinates) == Point:      # Переверяємо аргумент пееданий в конструктор на відповідність .
                                            
#             self.coordinates = coordinates  # Якщо умова виконається присвоїть полю *self.coordinates значення *coordinates # *Point(x,y) 
#         else:
#             print("Такий тип даних не підтримується") # Якщо ні принтимо це повідомлення .

#     def __getitem__(self, index): 
#         '''Магічний метод *__getitem__ , отримує один аргумент (ключ/індекс, по якому маємо повернуи потрібне нам значення)
#         і повертає відповідне значення , В нашому випадку реалізовано два ключа з значенням 0 і 1 , При всіх інших занченнях буде повертати *None'''
#         if index == 0 : # Перевіряємо чи наш ключ дорівнює 0 
#             return self.coordinates.x # Якщо умова виконалась повертаємо значення поля *x з відповідного поля екзепляру виду *Point(x,y) 
#         if index == 1 : # Перевіряємо чи наш ключ дорівнює 1
#             return self.coordinates.y  # Якщо умова виконалась повертаємо значення поля *y з відповідного поля екзепляру виду *Point(x,y)
        
#         #     raise IndexError("Невірний інфдекс") # у всіх інших випадках повертає *None абож можна викликати помилку з потрібним нам типом. Чи просто принт якийсь  
        

#     def __setitem__(self, index, value): 
#         '''Магічний метод *__setitem__ , отримує один два аргументи ,
#          ключ *index і значення *value яке потрібно перезаписати в відповідне поле.
#          В нашому випадку реалізовано два ключа з значенням 0 і 1 , При всіх інших занченнях буде повертати *None'''
#         if index == 0: # якщо ключ 0 , Перезаписати в полі *self.coordinates.x  значення на *value
#             self.coordinates.x = value
#         if index == 1:          # # якщо ключ 1 , Перезаписати в полі *self.coordinates.y  значення на *value
#             self.coordinates.y = value
                

# +++++++++++++++++++++++++++++++++++++++++++ Тестові значення і виклик функції (не потрібний для автоперевірки.) ++++++++++++++++++++++   

# vector = Vector(Point(1, 10))

# print(vector.coordinates.x)  # 1
# print(vector.coordinates.y)  # 10

# print(vector[0]) # 1

# vector[0] = 11  # Встановлюємо координату x вектора 11
# vector[5] = 15  # Встановлюємо не описаному ключу 5 значення 15 
# print(vector[0])  # 11
# print(vector[1])  # 10
# print(vector[5])  # *None (буде повертати якщо індекс не дорівнює 0 або 1)

# Примітка : Іншими словами,  магічні методи *__setitem__ і *__getitem__ 
# потрібно, щоб ми могли звернутись до потрібного нам поля класу красиво .  

# *vector[0] буде містити, то саме що і *vector.coordinates.x, а *vector[1] буде містити, то саме що і *vector.coordinates.y .


# ================================ Звдання 5 / Task 5 ======================================

# ================================  3. Методи str та repr  ==========================


# Коли ви в інтерактивному режимі роботи з Python хочете побачити вміст деякого об'єкта, 
# ви просто пишете його ім'я в консолі та інтерпретатор виводить рядком подання цього об'єкта.

# l = [1, 2]
# l
# У консолі ви побачите [1, 2].

# За цей механізм внутрішнього читального уявлення об'єктів відповідає магічний метод __repr__. 
# Цей метод приймає лише один аргумент (self звичайно) і повертати повинен рядок.

# Якщо ви хочете виводити у випадках, коли програма повинна відобразити об'єкт, 
# якусь корисну інформацію ви можете модифікувати цей метод. Наприклад, клас точки на площині в Декартових координатах:

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f'Point ({self.x}, {self.y})'


# a = Point(1, 9)
# a
# Виконайте цей код у консолі Python і ви побачите Point(1, 9).

# Дуже схожий на нього метод, який відповідає за те, як об'єкт конвертується в рядок — це метод __str__. 
# Коли ви викликаєте функцію str та передаєте їй якийсь об'єкт, то насправді, цей об'єкт викликається методом __str__.

# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'Hello! I am {self.name}'


# bill = Human('Bill')
# bill_str = str(bill)
# print(bill_str)  # Hello! I am Bill



# ++++++++++++++++++++++++++++++++++++++  Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Реалізуйте для класу Point та Vector магічний метод __str__. 
# Для класу Point метод повинен повертати рядок виду Point(x,y), а для класу Vector - рядок Vector(x,y), 
# як у прикладі нижче (замість x,y необхідно підставити значення координат екземпляра класу):

# point = Point(1, 10)
# vector = Vector(point)

# print(point)  # Point(1,10)
# print(vector)  # Vector(1,10)

# +++++++++++++++++++++++++++++++++++++   Код / Code ++++++++++++++++++++++++++++++++++++

# Примітка :  І з нового тут тільки магічний метод *__str__ який відповідає за формат (як будуть виглядати ) наш екзепляр 
            # Що б при приніт екзапяру *print(point) був потрібний нам вигляда *Point(1,10) , а не *<__main__.Point object at 0x000002591E90B620> 

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self): 
#        ''' Магічний метод , не приймає жодних аргументів, тільки імя самого екзепляру-*self , 
#        відповідає за те, що при спробі викликати екзепляр по імені,(через принт чи іншй якись спосіб) 
#        поверне  звичайну стрічку потрібного формату. Повертає наш екзепляр до красивого зрозумілого користувачу виду 
#        Тобто при спробі запринтити екзепляр print(*еземпляр_класу_Point) виведе на екран те,
#        що відобразить наш f-рядок # *Point(1,10), а не реальне ний вигляд екзепляру *<__main__.Point object at 0x000002591E90B620>    '''
#        return f'Point({self.x}, {self.y})' # Поверне *Point(1,10)
        

# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __str__(self):
#        ''' Магічний метод , не приймає жодних аргументів, тільки імя самого екзепляру-*self , 
#        відповідає за те, що при спробі викликати екзепляр по імені,(через принт чи іншй якись спосіб) 
#        поверне  звичайну стрічку потрібного формату. Повертає наш екзепляр до красивого зрозумілого користувачу виду 
#        Тобто при спробі запринтити екзепляр print(*еземпляр_класу_Vector) виведе на екран те,
#        що відобразить наш f-рядок # *Vector(1,10), а не реальне ний вигляд екзепляру *<__main__.Vector object at 0x000001493162B8F0> '''
       
#        return f'Vector({self.coordinates.x}, {self.coordinates.y})'


# # +++++++++++++++++++++++++++++++++++++++++++ Тестові значення і виклик функції (не потрібний для автоперевірки.) ++++++++++++++++++++++   

# point = Point(1, 10)
# vector = Vector(point)

# print(point)  # Point(1,10)
# print(vector)  # Vector(1,10)

# ================================ Звдання 6 / Task 6 ======================================

# ================================  5. Функтори, метод call  ==========================

# Функтори — це об'єкти, які поводяться як функції у тому сенсі, що їх можна викликати та передавати їм аргументи. 
# Функція у Python — це такий самий об'єкт, 
# але у ньому реалізовано метод __call__, який відповідає за синтаксис виклику з круглими дужками.

# class Adder:
#     def __init__(self, add_value):
#         self.add_value = add_value

#     def __call__(self, value):
#         return self.add_value + value


# two_adder = Adder(2)
# print(two_adder(5))  # 7
# print(two_adder(4))  # 6

# three_adder = Adder(3)
# print(three_adder(5))  # 8
# print(three_adder(4))  # 7
# В цьому прикладі ми створили клас Adder, у якого є метод __call__. 
# Тепер об'єкти цього класу можна викликати як функцію, надаючи їм аргументи. 
# Ці виклики будуть викликати метод __call__ у об'єктів класу Adder.

# ++++++++++++++++++++++++++++++++++++++  Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Для екземпляра класу Vector реалізуйте функтор. Створіть для класу Vector метод __call__.
# Він має реалізувати наступну поведінку:

# vector = Vector(Point(1, 10))

# print(vector())  # (1, 10)
# При виклику екземпляра класу як функції він повертає кортеж з координатами вектора.

# Якщо при виклику ми передаємо параметр число, 
# ми виконуємо добуток вектора на число — множимо кожну координату
# на вказане число та повертаємо кортеж з новими координатами вектора.

# vector = Vector(Point(1, 10))

# print(vector(5))  # (5, 50)
# +++++++++++++++++++++++++++++++++++++   Код / Code ++++++++++++++++++++++++++++++++++++

# Примітка :  І з нового тут тільки магічний метод *__call__(функтатор) 
             # Магічний метод, який дозволяє звертатись до імені екземпляру як до функції . 
             # Шаблон *імя_екзепляру() або *імя_екзепляру(*якесь_значення)
             # В реалізації методу описуємо що потрібно робити з переданими даними і який повертати результат



class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None): 
        '''Магічний метод який дозволяє звертатись до імені екземпляру як до функції .
        Шаблон *імя_екзепляру(), В нашому випадку реалізовано умову завдання.
        *імя_екзепляру(*якийсь аргумент)
           Якщо передано як аргумент число(тип *int) то повертаємо кортеж утворений з двох значень за схемою : 
                значення з поля *x і *y екзепляру класу, множимо на переданий аргумент *value. 
           Сформований за схемою кортеж повертаємо в тіло коду 
           Якщо аргумент не передано,абож він іншого типу ніж *int то повертаємо кортеж 
           утворений з поточних значень цих полів екземпляру без змін.'''
        if type(value) == int: # Умова чи переданий аргумент має тип *int
            cord_tuple = () # Створюємо пустий кортеж (можна і не створювати це для кращого усвідомлення що відбувається)
            cord_tuple = self.coordinates.x*value, self.coordinates.y*value # Створення конкретного кортежу за описаною вище схемою який будемо повертати з методу
                                        # Примітка : Кортеж створюється просто якісь зміній присвоюємо якісь значення обовязково через кому.
            return cord_tuple  # Повертаємо сформований кортеж з методу.
        else :
            cord_tuple = self.coordinates.x, self.coordinates.y  # Створення конкретного кортежу за описаною вище схемою який будемо повертати з методу
            return cord_tuple # Повертаємо сформований кортеж з методу.
        
    
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
    
# # +++++++++++++++++++++++++++++++++++++++++++ Тестові значення і виклик функції (не потрібний для автоперевірки.) +++++++++++
    
vector = Vector(Point(1, 10))  # Створення конкретного екзепляру класу *Vector з іменем *vector 
                               # який в полі *coordinates  буде містити  екзепляр класу *Point шаблону *Point(x,y)
                               # В нашому випадку: поле *x == 1 а поле *y == 10

print(vector())  # (1, 10) # Прінтимо виклик без переданого аргументу, *vector() магічного методу *__call__ 
                           # реалізованого в нашому класі. Виведе # (1, 10)

print(vector(5)) # (5, 50) # Прінтимо виклик з переданим аргументом 5, *vector(5) магічного методу *__call__ 
                           # реалізованого в нашому класі. Виведе # (5, 50)

print(vector("щось")) # (1, 10) # # Прінтимо виклик з переданим аргументом "щось", *vector("щось") магічного методу *__call__ 
                           # реалізованого в нашому класі. Виведе початкові значення # (1, 10)

print(vector)  # Vector(1,10) # Прінтимо результа роботи реалізованого методу __str__ .(Для себе як повторення попередніх завдань)
print(vector[0]) # Виведе *1  # Прінтимо результа роботи реалізованого методу __getitem__ .(Для себе як повторення попередніх завдань)
