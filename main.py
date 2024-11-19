from password_manager import choose_action
from account_management import create_account, update_password, retrieve_password, delete_account

def main():
    while True:
        if choose_action():
            break
    
    while True:
        print("\nOptions:")
        print("[1] ➤ Create Account")
        print("[2] ➤ Retrieve Password")
        print("[3] ➤ Update Password")
        print("[4] ➤ Delete Account")
        print("[5] ➤ Exit")
        print("-" * 40)
        
        choice = input("Choose an option: ").strip()
        if choice == '1':
            create_account()
        elif choice == '2':
            retrieve_password()
        elif choice == '3':
            update_password()
        elif choice == '4':
            delete_account()
        elif choice == '5':
            print("\nThank you for using Password Manager. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
