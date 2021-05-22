def num_translate(key):
    return new_dict.get(key)



key = input("Введите числительное от 0 до 10 прописью на агл. языке: ")

new_dict = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
                "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

print(num_translate(key))
