investitions = int(input("Введите число: "))
Mike = int(input("Введите число: "))
Ivan = int(input("Введите число: "))
if Mike >= investitions and Ivan >= investitions:
    print(2)
elif Mike >= investitions:
    print("Только Майкл может вкладывать")
elif Ivan >= investitions:
    print("Только Иван может вкладывать")
elif Mike + Ivan >= investitions:
    print(1)
else:
    print("Никто не может вкладывать")