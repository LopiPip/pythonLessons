

# for - используется для списков



students = ["Pupik", "Dupik", "Karatutik", "Owner", "Kissa"]

# Проход по списку и печать каждого значения
for f in students:
    print(f)

# Добавляем Engineer конкретному значению списка. Вывод всех значений.
for f in students:
    if f == "Dupik":
        var = "Engineer " + f
        print(var)
    print(f)

# for f in students[:3]:
#     print(f)

for f in students:
    print(len(f))