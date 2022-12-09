import os
file_list=[]


def path_cheker(folder, file_list=None):
    if file_list is None:
        file_list = []
    for item in os.listdir(folder):
        full_path=os.path.join(folder, item)
        if os.path.isfile(full_path):
            file_list.append(full_path)
        else:
            os.path.isdir(full_path)
            path_cheker(full_path, file_list)
    return file_list


test_folder="C:\\movie"
print(path_cheker(test_folder))
