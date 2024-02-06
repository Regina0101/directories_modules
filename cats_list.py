from pathlib import Path

path = Path('cats/path.txt')

def get_cats_info(path):
    with open(path, 'r') as fh:
        content = fh.readlines()

    keys_list=["id", "name", "age"]
    cats_info=[]
    for lines in content:
        line = lines.split(',')
        cleaned_list = [item.replace('\n', '') for item in line]
        cats_list = dict(zip(keys_list, cleaned_list))
        cats_info.append(cats_list)

    return cats_info


cats_info = get_cats_info(path)
print(cats_info)
