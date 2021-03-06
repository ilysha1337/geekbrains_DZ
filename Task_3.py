"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

# Сложность О(n)
company = {'Apple': 100, 'Google': 100, 'Samsung': 7, 'Nokia': 30, 'Xiaomi': 80, 'MVM': 10}
i = 3 #
while i != 0:
    result = [(v, k) for k, v in company.items()]
    print(max(result))
    company.pop(max(result)[1])
    i -= 1

print("*"*40)

# Сложность О(n 2 log n)
company = {'Apple': 100, 'Google': 100, 'Samsung': 7, 'Nokia': 30, 'Xiaomi': 80, 'MVM': 10}
result = []
for i, j in company.items():
    revers = [j, i]
    result.append(revers)
    result.sort(reverse= True)
print(result[:3])


# Отдаем предпочтение первому варианту так как сложность ниже. Во втором варианте в цикле имеется метод sort, который
# достаточно "тяжелый", а в совокупности с циклом делает решение "неподъемным". Если бы у нас были миллионы компаний,
# нас бы за такое решение уволили. )))