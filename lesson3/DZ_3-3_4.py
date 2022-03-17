def thesaurus_2(*args):
    my_dict = {}
    for i in args:
        name, surname = i.split(" ")
        new_dict = my_dict.setdefault(surname[0], {})
        new_list = new_dict.setdefault(name[0], [])
        new_list.append(i)

    return my_dict


print(thesaurus_2('Иван Иванов', 'Иван Петров', 'Олег Медведев', 'Егор Дмитриченко', 'Даша Шульгина', 'Илья Жирков',
                  'Клава Кока', 'Коля Кока', 'Ольга Кока', 'Елена Кока'))
