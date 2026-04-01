class User:
    def __init__(self,  email):
        self.email = email
    def show_email(self):
        print(self.email)

user = User("test@mail.com")
user.show_email()


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
print(account.balance)

class Cart:
    def __init__(self):
        self.item = []

    def add_item(self, item):
        self.item.append(item)
    def total_items(self):
        return len(self.item)

cart = Cart()
cart.add_item("Laptop")
cart.add_item("Mouse")

print(cart.total_items())



class BaseApi:
    def request(self):
     print("Base request")

class UserAPI(BaseApi):
    def request(self):
        print("User request")

api1 = BaseApi()
api1.request()

api2 = UserAPI()
api2.request()


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class AdminUser(User):
    def __init__(self, email, password, role):
        super().__init__(email, password)
        self.role = role


admin = AdminUser("admin@mail.com", "123456", "admin")
print(admin.email)
print(admin.password)
print(admin.role)


