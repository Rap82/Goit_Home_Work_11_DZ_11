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


