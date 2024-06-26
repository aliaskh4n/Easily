import os

# Создаем список файлов и каталогов для создания
files_and_dirs = [
    './app.py',
    './templates/base.html',
    './templates/index.html',
    './templates/situation.html',
    './templates/add_situation.html',
    './templates/add_word.html',
    './templates/edit_situation.html',
    './templates/edit_word.html',
    './static/css/styles.css',
    './static/js/scripts.js',
    './models.py',
    './forms.py'
]

# Создаем каждый файл и каталог
for item in files_and_dirs:
    if '.' in item:  # это файл
        os.makedirs(os.path.dirname(item), exist_ok=True)  # создаем папки для файла, если их нет
        with open(item, 'w') as f:
            f.write('')  # создаем пустой файл
    else:  # это каталог
        os.makedirs(item, exist_ok=True)

print("Файлы и каталоги успешно созданы.")
