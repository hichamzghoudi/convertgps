import os

def print_folders(root_path, prefix=""):
    folders = [f for f in sorted(os.listdir(root_path))
               if os.path.isdir(os.path.join(root_path, f))]

    for index, folder in enumerate(folders):
        path = os.path.join(root_path, folder)
        is_last = index == len(folders) - 1

        if is_last:
            connector = "└── "
            new_prefix = prefix + "    "
        else:
            connector = "├── "
            new_prefix = prefix + "│   "

        print(prefix + connector + folder)
        print_folders(path, new_prefix)

# غيّر المسار إلى مجلد مشروعك
project_path = r"C:\xampp\htdocs\convertgps"
print(project_path)
print_folders(project_path)
