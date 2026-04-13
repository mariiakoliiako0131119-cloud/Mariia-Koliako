class TestRunStats:
    def __init__(self, failed_tests=None):
        self.failed_tests = failed_tests = []

    def add_failed_test(self, test_name: str):
        self.failed_tests.append(test_name)

    def add_failed_tests(self, test_names: list[str]):
        self.failed_tests.extend(test_names)

    def  get_failed_tests(self) -> list[str]:
        return self.failed_tests

    def get_failed_count(self) -> int:
        return len(self.failed_tests)

run1 = TestRunStats()
run2 = TestRunStats()

run1.add_failed_test("test_create_user")
run1.add_failed_tests(["test_delete_user", "test_update_user"])

print(run1.get_failed_tests())
print(run1.get_failed_count())
print(run2.get_failed_tests())


class  EnvironmentConfig:
    DEFAULT_TIMEOUT = 30

    def __init__(self,  env_name,  base_url,  api_key):
        self.env_name = env_name
        self.base_url = base_url
        self._api_key = api_key

    @property
    def api_key_masked(self):
        return self._api_key[:3] + "***"

    @property
    def base_api_url(self):
        return self.base_url

    @staticmethod
    def is_valid_url(url):
        if url[:4] == "http":
            return True
        else:
            return False

    @classmethod
    def get_default_timeout(cls):
        return  cls.DEFAULT_TIMEOUT

config = EnvironmentConfig("stage", "https://stage.api.test.com", "abcdef123456")

print(config.base_api_url)
print(config.api_key_masked)
print(EnvironmentConfig.is_valid_url("https://test.com"))
print(EnvironmentConfig.get_default_timeout())


class Logger:
    def log(self, message: str):
        print(f"[LOG] {message}")

class TestReporter:
    def __init__(self):
        self.logger = Logger()
        self.results = []

    def add_result(self, test_name: str, status: str):
        result = test_name + " " + status
        self.logger.log(result)
        self.results.append(result)

    def show_results(self):
        for result in self.results:
            print(result)


reporter = TestReporter()
reporter.add_result("test_login", "passed")
reporter.add_result("test_delete_user", "failed")
reporter.show_results()


class DictDataSource:
    def __init__(self, data: dict):
        self.data = data

    def get_data(self):
        return self.data

class MockDataSource:
    def get_data(self):
        return {"email": "mock@test.com", "password": "123456"}

def prepare_login_data(data_source):
    data = data_source.get_data()
    print("keys:", list(data.keys()))
    return data

def transform_data(func):
    data = func()
    return {k: v.upper() if isinstance(v, str) else v for k, v in data.items()}


real_source = DictDataSource({"email": "user@test.com", "password": "qwerty"})
mock_source = MockDataSource()

real_source = DictDataSource({"email": "user@test.com", "password": "qwerty"})
mock_source = MockDataSource()
print(prepare_login_data(real_source))
print(prepare_login_data(mock_source))
print(real_source.get_data())
print(mock_source.get_data())
upper_data = transform_data(mock_source.get_data)
print(upper_data)

from abc import abstractmethod
from abc import ABC

class BaseCheck(ABC):
    @abstractmethod
    def check(self, response: dict):
        pass


class StatusCodeCheck(BaseCheck):
    def __init__(self, expected_status_code):
        self.expected_status_code = expected_status_code

    def check(self, response: dict):
        return response["status_code"] == self.expected_status_code

class RequiredFieldCheck(BaseCheck):
    def __init__(self, field_name):
        self.field_name = field_name

    def check(self, response: dict):
        return self.field_name in response['body']

def run_checks(checks, response):
    return [check.check(response) for check in checks]


response = {
    "status_code": 200,
    "body": {
        "id": 1,
        "name": "Daniil"
    }
}

checks = [
    StatusCodeCheck(200),
    RequiredFieldCheck("id"),
    RequiredFieldCheck("email")
]

results = run_checks(checks, response)
print(results)

status_check = StatusCodeCheck(200)
field_check_id = RequiredFieldCheck("id")
field_check_email = RequiredFieldCheck("email")

print(status_check.check(response))
print(field_check_id.check(response))
print(field_check_email.check(response))






