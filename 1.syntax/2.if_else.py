#  ***** логические операторы НЕ (NOT), И (AND), ИЛИ (OR) *****

x = True
y = False

# оператор НЕ
# print(not x)

# оператор И - возвращает true только если значения обеих переменных равны true

res = x and y

# res = True and True

# оператор ИЛИ - возвращает false только если значения обеих переменных равны false

res = False or False

# print(res)


# *** Условные операторы ***

# if True: 
#     c = "Hello!"
#     print(c)

a = 0

# if a > 0:
#     print("больше 0")
# elif a == 0:
#     print("равно 0")
# else:
#     print(" меньше 0")

b = 'С'

if b == 'A':
    c = "равно A"
elif b == 'Б':
    c = "равно Б"
elif b == 'B':
    c = "равно B"
else:
    c = "не знаю"

# print(c)

# *** условная задача "термостат"

# текущая температура
cur_temp = 7
# целевые значения теипература (установленная через ручку регулятора)
tar_temp_1 = 27
tar_temp_2 = 10
# дополнительная условие - "зависимость от присутствия людей"
z = False

# логика термостата
if z == True and cur_temp < tar_temp_1:
    print(f"Включено нагревание до { tar_temp_1}")
elif z == False and cur_temp < tar_temp_2:
    print(f"Включено нагревание до { tar_temp_2}")
else:
    print("Выключение нагревания")