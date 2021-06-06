import os

new_dict = {'my_project': [{'setings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for key, el in new_dict.items():
    if not os.path.exists(key):
        for i in el:
            for tmp in i.keys():
                os.makedirs(os.path.join(key, tmp))
