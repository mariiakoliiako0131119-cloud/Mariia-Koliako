users = [
    {
        "id": 101,
        "name": "Alice"
    },
    {
        "id": 102,
        "name": "Bob"
    },
    {
        "id": 103,
        "name": "Kate"
     }
]

user_ids = [user['id'] for user in users]
print(user_ids)


orders = [
    {
        "id": 1,
        "status": "created"
    },
    {
        "id": 2,
        "status": "paid"
    },
    {
        "id": 3,
        "status": "cancelled"
    },
    {
        "id": 4,
        "status": "paid"
    }
]

paid_orders = [order for order in orders if order["status"] == "paid"]
print(paid_orders)

response = {
    "orders": [
    {
        "items":
            ["apple", "banana"]
    },
    {
        "items":
         ["milk", "bread"]
     }
    ]
 }

items = [item for order in response["orders"] for item in order["items"]]
print(items)

def log_test(func):
    def wrapper():
        print('Start func')
        func()
        print('End func')
    return wrapper


@log_test
def login_test():
    print("Login step")

login_test()

def test_logger(func):
    def wrapper():
        print(f"Running test: {func.__name__}")
        func()
    return wrapper


@test_logger
def test_create_user():
    print("Create user step")

test_create_user()

def log_args(func):
    def wrapper(*args):
        print("Arguments", *args)
        return func(*args)
    return wrapper


@log_args
def add(a, b):
    return a + b

add(2, 3)


def is_admin(func):
    def wrapper(user, *args, **kwargs):
        if not user["is_admin"]:
            print("Access denied")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@is_admin
def get_orders(user):
    print(f"Order list {user['name']}")

user1 = {"name": "Daniil", "is_admin": True}
user2 = {"name": "Alex", "is_admin": False}

get_orders(user1)
get_orders(user2)















