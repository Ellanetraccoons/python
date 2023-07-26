def f1():
    try:
        num = int(input("Введите целое пятизначное число: "))
        if len(str(num)) != 5:
            raise Exception()
    except:
        print("Число введено неверно!")
        f1()
    else:
        t = num
        #step 1
        t = float(((num % 100)//10)**(num % 10)) 
        print(t)
        #step 2
        t *= float(((num % 1000)//100))
        print(t)        
        #step 3
        t /= float(((num//10000)-((num//1000)%10)))
        print(t)
f1()
