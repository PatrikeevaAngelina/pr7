a = input("Введите целое простое число a: ")
b = input("Введите целое простое число b: ")
c = input("Введите целое простое число c: ")

if a.isdigit() and b.isdigit() and c.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)
    result = a+b*4-c
        print(f"Результат в десятичной системе: {result}")
else:
    print("Ошибка: введите корректные целые числа")