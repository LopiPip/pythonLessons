pin = 1234

print("Бонжур, епт! Введи пин:")
user_pin = int(input())

if pin == user_pin:
    print("Какую сумму снять?")
else:
    print("ПНХ! Осталось 2 попытки")
    user_pin = int(input())
    if pin == user_pin:
        print("Какую сумму снять?")
    else:
        print("ПНХ! Осталось 1 попытка")
        user_pin = int(input())
        if pin == user_pin:
            print("Какую сумму снять?")
        else:
            print("ПНХ! Карту заблочил, наберешь.")