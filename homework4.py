def is_integer(s):
    return s.isdigit()
a = input("Введите значение a: ")
b = input("Введите значение b: ")
c = input("Введите значение c: ")
if is_integer(a) and is_integer(b) and is_integer(c):
    a = int(a)
    b = int(b)
    c = int(c)
    x = a + b * 4 - c
    print(f"Решение уравнения x = a + b * 4 - c : x = {x}")
else:
    print("Ошибка: Введены некорректные данные. Введите целые числа.")
