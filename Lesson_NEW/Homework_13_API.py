import requests
import random

BASE_URL = "https://api.bank.easyitlab.tech"

def login():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json = {
            "email": "mariya_kolyako@mail.ru",
            "password": "Fh3VZQEkzZX8"
    },
        headers={
         "Content-Type": 'application/json'
    }
)
    assert response.status_code == 200, "Данные указаны не верно"
    response_json = response.json()
    assert 'access_token' in response_json

    print(response.status_code)
    print(response_json)

    token = response_json.get('access_token')
    assert token, "Token not found"
    return token

token = login()

HEADERS = {
    "Authorization": f"Bearer {token}",
     "Content-Type": 'application/json'
}

get_all_employees = requests.get(
    f"{BASE_URL}/students/employees",
    headers=HEADERS
)
assert get_all_employees.status_code == 200
get_all_employees_json = get_all_employees.json()
assert isinstance(get_all_employees_json, list)
for employee in get_all_employees_json:
    assert 'id' in employee
    assert 'email' in employee
    assert 'full_name' in employee

print("Задание 2 - все проверки прошли!")

def create_employee():
    random_number = random.randint(1000, 9999)
    body = {
        "email": f"employee.{random_number}.demo@demobank.local",
        "full_name": "Иван Петров",
        "password": "employee123"
    }

    created_employee = requests.post(
        f"{BASE_URL}/students/employees",
        json=body,
        headers=HEADERS
    )
    assert created_employee.status_code == 200
    created_employee_json = created_employee.json()

    assert created_employee_json['email'] == body["email"]
    assert created_employee_json['full_name'] == body['full_name']
    assert "id" in created_employee_json
    print("Задание 3 - все проверки прошли!")
    return created_employee_json["id"], created_employee_json["email"]

employee_id, employee_email = create_employee()

get_employee = requests.get(
    f"{BASE_URL}/students/employees/{employee_id}",
    headers=HEADERS
)
assert get_employee.status_code == 200
get_employee_by_id_json = get_employee.json()

assert get_employee_by_id_json["id"] == employee_id
assert get_employee_by_id_json['email'] == employee_email
print("Задание 4 - все проверки прошли!")

def update_employee():
    body = {
        "email": "updated@demobank.local",
        "full_name": "Updated User"
    }
    updated_employee = requests.patch(
        f"{BASE_URL}/students/employees/{employee_id}",
        json=body,
        headers=HEADERS
    )
    assert updated_employee.status_code == 200
    updated_employee_json = updated_employee.json()

    assert updated_employee_json['email'] == "updated@demobank.local"
    assert updated_employee_json['full_name'] == "Updated User"
    print("Задание 5 - все проверки прошли!")

update_employee()

def delete_employee(employee_id):
    deleted_employee = requests.delete(
        f"{BASE_URL}/students/employees/{employee_id}",
        headers=HEADERS
    )

    assert deleted_employee.status_code == 200
    print("Задание 6 - сотрудник удален!")


    get_deleted_employee = requests.get(
        f"{BASE_URL}/students/employees/{employee_id}",
        headers=HEADERS
    )
    assert get_deleted_employee.status_code == 404 or get_deleted_employee.status_code == 422
    print("Задание 6 - все проверки прошли!")

delete_employee(employee_id)

def create_employee_without_email():
    body = {
        "full_name": "Иван Петров",
    }

    created_employee_without_email = requests.post(
        f"{BASE_URL}/students/employees",
        json=body,
        headers=HEADERS
    )
    assert created_employee_without_email.status_code == 422
    print("Задание 7.1 - все проверки прошли!")

create_employee_without_email()

def  get_employees_without_token():
    headers_without_token = {
        "Content-Type": 'application/json'
    }

    response = requests.get(
        f"{BASE_URL}/students/employees",
        headers=headers_without_token
    )
    assert response.status_code == 401
    print("Задание 7.2 - все проверки прошли!")

get_employees_without_token()

get_employee_invalid_id = requests.get(
    f"{BASE_URL}/students/employees/invalid_id",
    headers=HEADERS
)
assert get_employee_invalid_id.status_code in [422, 404]
print("Задание 7.3 - все проверки прошли!")

get_employee_status = requests.get(
    f"{BASE_URL}/students/clients?status=ACTIVE",
    headers=HEADERS
)
assert get_employee_status.status_code == 200
get_employee_status_json = get_employee_status.json()
assert isinstance(get_employee_status_json, list)
assert all("status" in client for client in get_employee_status_json)
assert all(client["status"] == "ACTIVE" for client in get_employee_status_json)
print("Задание 8 - все проверки прошли!")

def test_employee_lifecycle():
    token = login()
    headers= {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    random_number = random.randint(1000, 9999)
    create_response = requests.post(
        f"{BASE_URL}/students/employees",
        json={"email": f"employee.{random_number}.demo@demobank.local",
              "full_name": "Иван Петров",
              "password": "employee123"},
        headers=headers
    )
    assert create_response.status_code == 200
    employee_id = create_response.json()["id"]

    get_response = requests.get(
        f"{BASE_URL}/students/employees/{employee_id}",
        headers=headers
    )
    assert get_response.status_code == 200

    update_response = requests.patch(
        f"{BASE_URL}/students/employees/{employee_id}",
        json={
            "full_name": "Updated User",
            "email": f"updated.{random_number}@demobank.local"
        },
        headers=headers
    )
    assert update_response.status_code == 200

    delete_response = requests.delete(
        f"{BASE_URL}/students/employees/{employee_id}",
        headers = headers
    )
    assert delete_response.status_code == 200

    print("Задание 9 - все проверки прошли!")

test_employee_lifecycle()


