import hashlib
import json
import os

# دالة لتشفير كلمة المرور باستخدام SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# دالة لحفظ البيانات في ملف JSON
def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# دالة لتحميل البيانات من ملف JSON
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}  # إرجاع قاموس فارغ إذا لم يكن الملف موجودًا
