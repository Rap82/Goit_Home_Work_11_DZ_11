# class A:
#     def __init__(self, count) -> None:
#         self.count = count
#     def __eq__(self, other): # Магічний метод який дозволяє порівнювати обєкти одного класу .
#         return isinstance(other, A) and self.count == other.count
# a = A("aaa")
# b = A("bbb")
# c = A("ccc")
# my_list = [ a, b, c, ] # Список Обєктів class A
# print(f"список обэктів my_list = {my_list}")
# str_input = input("Введіть якесь значення \n # aaa, bbb, ccc\n") # Звичайний input повертає *str
# # (Для правильного результату вводим тестові значення ааа або bbb або ccc )
# str_input = A(str_input) # Приведення до типу class A
# if str_input in my_list:  # Пошук обєкту *str_input class A, в списку *my_list обєктів
#     print(f"Є таке значення в списку my_list = {my_list}" )
# else :
#     print(f"Немає такого значення в списку my_list = {my_list}" ) 

class SomeClass:

    somestatic = "Статичне_поле *somestatic"
	
    def __init__(self, some_argument): # Конструктор класу який приймає один обовязковий аргумент.
        self.number = some_argument
        self.dubell_number = 2*some_argument
        self.change_number = 2*self.dubell_number + self.number 
        self.str_number = str(some_argument)+"ff"
        self.str_number_repit_str_number = self.str_number
        


some = SomeClass(10) # Створення конкретного екзепляру з іменем *some, class SomeClass з початковим значенням  10
                     # Оскільки в констуркторі __init__ класу в нас після self , якийсь аргумент *some_args, 
                     # то при створені екзепляру класу ми в круглих душках обовязково маємо передати якесь значення 
print(some.number)
some.number = 12
print(some.number)
print(some.dubell_number)
print(some.change_number)
some.number = some.number + 5
print(some.number)
print(some.str_number)
print(some.str_number_repit_str_number)
print(some.somestatic)