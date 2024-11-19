import getpass
from hash_utils import hash_password, save_data, load_data
from display_utils import display_title

# دالة لإنشاء حساب جديد
def create_account():
    display_title("Create New Account")
    account = input("Enter account name (e.g., Google, Twitter): ").strip()
    
    data = load_data('passwords.json')
    if account not in data:
        data[account] = {}
    
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    
    if password != confirm_password:
        print("⚠️ Passwords do not match. Try again.")
        return
    
    hashed_password = hash_password(password)
    data[account] = hashed_password
    save_data(data, 'passwords.json')
    print(f"✅ Password for '{account}' saved successfully.")

# دالة لتحديث كلمة المرور لحساب معين
def update_password():
    display_title("Update Password")
    account = input("Enter account name to update: ").strip()
    data = load_data('passwords.json')
    
    if account in data:
        password = getpass.getpass("Enter new password: ")
        confirm_password = getpass.getpass("Confirm new password: ")
        
        if password != confirm_password:
            print("⚠️ Passwords do not match. Try again.")
            return
        
        hashed_password = hash_password(password)
        data[account] = hashed_password
        save_data(data, 'passwords.json')
        print(f"✅ Password for '{account}' updated successfully.")
    else:
        print("⚠️ Account not found.")

# دالة لاسترجاع كلمة المرور المشفرة لحساب معين
def retrieve_password():
    display_title("Retrieve Password")
    account = input("Enter account name to retrieve: ").strip()
    data = load_data('passwords.json')
    
    if account in data:
        print(f"🔒 Hashed Password for '{account}': {data[account]}")
    else:
        print("⚠️ Account not found.")

# دالة لحذف حساب معين
def delete_account():
    display_title("Delete Account")
    account = input("Enter account name to delete: ").strip()
    data = load_data('passwords.json')
    
    if account in data:
        confirm = input(f"Are you sure you want to delete the account '{account}'? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del data[account]
            save_data(data, 'passwords.json')
            print(f"✅ Account '{account}' deleted successfully.")
        else:
            print("❌ Deletion cancelled.")
    else:
        print("⚠️ Account not found.")
