import shutil
import os

# المجلد الرئيسي
root = r"C:\xampp\htdocs\convertgps"

# مجلد واجهة الويب للتطبيق
web_dir = os.path.join(root, "gpsapp")

# الملفات المراد نقلها
files_to_copy = [
    "index.html",
    "style.css",
    "ville.json",
    "convertgps.png",
    "modelcsvnw.JPG",
    "modelcsvxy.JPG"
]

for f in files_to_copy:
    src = os.path.join(root, f)
    dst = os.path.join(web_dir, f)
    if os.path.exists(src):
        shutil.copy2(src, dst)  # copy2 يحتفظ بالتاريخ الأصلي
        print(f"Copied {f} → gpsapp/")
    else:
        print(f"{f} not found in root!")

print("\n✅ All files copied to gpsapp successfully.")
