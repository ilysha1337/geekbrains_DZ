import itertools

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Poll', 'Kate']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = itertools.zip_longest(tutors, klasses, fillvalue=None) if len(tutors) > len(klasses) else zip(tutors, klasses)

print(next(result))
print(next(result))
print(*itertools.islice(result, 7))
