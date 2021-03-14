# *** Циклы (операторы циклов) ***

# Оператор цикла while

# бесконечный цикл (прерывается ctrl+c)
# while True:
#   print("Hi")


# бесконечный цикл while с прерыванием
# while True:
#     _in_data = input("Введите что-нибудь: ")
#     if _in_data == "stop":
#         print("Buy buy!")
#         break
#     print("Hi")


# Цикл с условием

#number = 0

# while number <= 10:
#     print(f"Number: {number}")
#    # number = number + 2 # инкремент
#     number += 2

#number_2 = 10

# while number_2 > 0:
#     print(f"Number: {number_2}")
#     number_2 -= 1 # декремент


# цикл с условием и с прерыванием

# number_3 = 0
# treshold = 7

# while number_3 < 15:
#      print(f"Num: {number_3}")
#      if number_3 == treshold:
#          print("Loop terminated")
#          break
#      number_3 += 1


# Оператор цикла for

# 1. читает значение элнмент итерируемого объекта по порядку
# 2. присваивает это значение в свою переменную
# 3. выполняет блок кода своего тела

# for item in [10,20,30,40,50]:
#     print(item)

my_str = "Hello!"

# for char in my_str:
#     print(char*3)

my_list = [10,20,30,40,50]
my_list_2 = []

# for i in my_list:
#     # i += 2
#     res = i **2
#     my_list_2.append(res)

# for i in my_list[::-1]:
#     res = i **2
#     my_list_2.append(res)

# for i in range(0, 20):
#     print(i)

# for i in range(20):
#     print(i)

# с безымянной переменной (_)
# for _ in range(5):
#     print("Hi")

for val in range(10, 100, 10):
    if val == 50:
        break
    print(val)