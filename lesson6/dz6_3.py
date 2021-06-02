from itertools import zip_longest

with open("users.csv", 'r', encoding='utf-8') as f:
    users = ([i.replace('\n', '') for i in f])

with open("hobby.csv", 'r', encoding='utf-8') as f:
    hobby = ([i.replace('\n', '') for i in f])

if len(users) < len(hobby):
    exit(1)

result = dict(zip_longest(users, hobby))

with open("user_hobby.txt", 'w', encoding="utf-8") as f:
    f.write(str(result))
