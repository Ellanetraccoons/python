def f1():
    try:
        num = int(input("Введите целое число: "))
    except:
        print("Число введено неверно!")
        f1()
    else:
        msg = ""
        
        #check 1
        if num > 0:
            msg += "Положительное "
        elif num == 0:
            print("Нулевое число")
        else:
            msg += "Отрицательное "
        
        #check 2
        if (num % 2) == 0 and num != 0:
            msg += "чётное число"
        elif num != 0:
            msg += "нечётное число"
        
        print(msg)
f1()