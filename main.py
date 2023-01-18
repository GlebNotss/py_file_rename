import os

path = r"/home/gleb/Desktop/projects/py_file_rename/img/"

i = 1

for file_name in os.listdir(path):
    base_name, ext = os.path.splitext(file_name) 
    base_name = base_name.strip().split(" ")
    new_name = ("-").join(base_name).lower()

    if ext.lower() not in ['.svg', '.jpeg', '.png']:
        continue

    abs_file_name = os.path.join(path, file_name)

    new_abs_file_name = os.path.join(path, new_name + '.blade.php')
    print(new_abs_file_name)
    os.rename(abs_file_name, new_abs_file_name)
    i += 1