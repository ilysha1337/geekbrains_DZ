my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

tmp = 0
for i in range(len(my_list)):
    i = i + tmp
    if my_list[i][-1].isdigit():
        if my_list[i][0] in "+-":
            my_list[i] = f"{my_list[i][0]}{int(my_list[i][-1]):02}"
        else:
            my_list[i] = f"{int(my_list[i]):02}"
        my_list.insert(i, "'")
        my_list.insert(i + 2, "' ")
        tmp = tmp + 2
    else:
        my_list[i] = f"{my_list[i]} "

print(my_list)

print("".join(my_list))