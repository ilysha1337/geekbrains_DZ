def num_translate_adv(word):
    if word[0].isupper():
        word_up = my_dict.get(word.lower())
        result = word_up.capitalize()
    else:
        result = my_dict.get(word)
    return result


my_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

number_str = input("Введите прописью число от 0 до 10 на англ. языке: ")

print(num_translate_adv(number_str))
