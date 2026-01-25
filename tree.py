import os

ROOT = r"C:\xampp\htdocs\convertgps"

if not os.path.exists(ROOT):
    print("[PATH NOT FOUND]")
else:
    try:
        entries = os.listdir(ROOT)
    except PermissionError:
        print("[NO ACCESS]")
        entries = []

    for name in entries:
        full_path = os.path.join(ROOT, name)
        if os.path.isdir(full_path):
            print(f"[DIR ] {name}")
        else:
            print(f"[FILE] {name}")
