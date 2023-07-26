def f1():
    try:
        x = float(input("Введите минимальную сумму инвестиций: "))
        a = float(input("Введите сумму Майкла в долларах: "))
        b = float(input("Введите сумму Ивана в долларах: "))
    except:
        print("Сумма введена неверно!")
        f1()
    else:
        if a >= x and b >= x:
            print(2)
        elif a >= x and b < x:
            print("Mike")
        elif a < x and b >= x:
            print("Ivan")
        elif (a + b) >= x:
            print(1)
        elif (a + b) < x:
            print(0)
f1()