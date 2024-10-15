def convert(n):
    if n < 5:
        return str(n)
    else:
        return convert(n // 5) + str(n % 5)
x = input("Введите целое десятичное число: ")
if x.isdigit():
    x = int(x)
    print(f"Пятеричная система счисления: {convert(x)}")
else:
    print("Ошибка: введите корректное число.")