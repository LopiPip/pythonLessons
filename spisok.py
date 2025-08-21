personal = ["Pupkin", "Dupkin", "Krasavec"]

print(personal[0])

# print(len(personal)) # считает колво сущностей в списке
# print(personal[-1])
# print(personal[-1:2])

num = ["1", "2", "3"]
# personal.append("Fedor") # добавляет Федора в список


print(personal)

# pn = []
# pn.append(personal)
# pn.append(num)
# pp = personal + num
#
# print(pn)
# print(len(pn))
# print(pp)
print(personal)
print(num)

obbb = zip(personal, num)
print(list(obbb))

numbers_list = [1, 2]
str_list = ['one', 'two']
result = zip(numbers_list, str_list)    # Передаем в метод названия списков, которые хотим объединить
print(list(result))
