import os
from collections import defaultdict
import django

r_dirs = django.__path__[0]
dj_files = defaultdict(int)
for root, dirs, files in os.walk(r_dirs):
    for i in files:
        size = 10 ** len(str(os.stat(os.path.join(root, i)).st_size))
        dj_files[size] += 1
for size, result in sorted(dj_files.items()):
    print('Размер: {} кол-во: {}'.format(size, result))
