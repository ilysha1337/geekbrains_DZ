# Задча 5-1
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
new_str = ''
new_list = []

for i in prices:
    rub = int(i)
    result = f"{rub:02} руб {(int(i*100)%100):02} коп"
    new_str +=result + ", "
    new_list.append(result)
print(new_str) #Вывод ввиде строки
print(new_list) #Вывод в виде списка

# Задача 5-2
print(id(new_list))
new_list.sort()
print(new_list)
print(id(new_list))

# Задача 5-3

sorted_list = sorted(new_list, reverse=True)
print(sorted_list)
print(id(sorted_list))

# Задача 5-4
print(sorted_list[0:5])
