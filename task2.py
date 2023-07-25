
error = str("Неправильно! Попробуй ещё раз! Неправильно написанные этапы: ")
print(len(error))
correct = str("Всё верно! Молодец!")

part1 = input("Введите первый этап развития человека: ")
if part1 != "Australopithecus":
    error += "первый, "
    part1 = "Australopithecus"

part2 = input("Введите второй этап развития человека: ")
if part2 != "Homo Habilis":
    error += "второй, "
    part2 = "Homo Habilis"

part3 = input("Введите третий этап развития человека: ")
if part3 != "Homo Erectus":
    error += "третий, "
    part3 = "Homo Erectus"
part4 = input("Введите четвёртый этап развития человека: ")
if part4 != "Homo Neanderthalensis":
    error += "четвёртый, "
    part4 = "Homo Neanderthalensis"

part5 = input("Введите пятый этап развития человека: ")
if part5 != "Homo Sapiens":
    error += "пятый "
    part5 != "Homo Sapiens"
    
if len(error) > 61:
    print()
    print(error)
    print("Правильный порядок:")
    print(part1, part2, part3, part4, part5, sep=' => ')
else:
    print()
    print(correct)
    print(part1, part2, part3, part4, part5, sep=' => ')

"""
 Правильные ответы:
 
 Australopithecus – Homo Habilis –
 Homo Erectus – Homo Neanderthalensis –
 Homo Sapiens
 
"""
