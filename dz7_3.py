from os import walk, path, listdir
from shutil import copytree

name = 'new_project'

try:
    for root, dirs, files in walk(name):
        if 'templates' in dirs and root != name:
            for entry in listdir(path.join(root, "templates")):
                copytree(path.join(root, 'templates', entry), path.join(name, 'templates', path.basename(root)))
except FileExistsError:
    print('error')
