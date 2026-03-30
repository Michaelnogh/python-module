accounts = [
    {"account_id": 100, "name": "Liron", "pin": "1234", "balance": 500},
    {"account_id": 101, "name": "Daniel", "pin": "5678", "balance": 900},
]

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "12345"


def find_account(account_id):
    for account in accounts:
        if account_id == account["account_id"]:
            return account
    return None


user_pin_input = int(input("Pass here your PIN"))
def verify_pin(account , user_pin_input):
    is_pin_correct = account["pin"] == user_pin_input
    
    return is_pin_correct
    pass


def deposit():
    account_id = int(input("Enter Your Account number"))
    user_pin_input = int(input("pass here your PIN")
                         )
account = find_account(account_id)

def withdraw():
    pass


def create_account():
    pass


def show_all_accounts():
    pass


def admin_login():
    username = input("Admin username: ")
    password = input("Admin Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    
    print("Access denied")

is_admin_in = admin_login()

print(f"Admin is in? : {is_admin_in} ")