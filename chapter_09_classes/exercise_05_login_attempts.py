
class User:

    def __init__(self, user_name, first_name, last_name):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe(self):
        print(f"User: {self.user_name}")
        print(f"\tFirst Name    : {self.first_name.title()}")
        print(f"\tLast Name     : {self.last_name.title()}")
        print(f"\tLogin Attempts: {self.login_attempts}")
        print("---")


user = User(user_name="alanderer",
            first_name="andreas",
            last_name="landerer")
user.describe()
user.increment_login_attempts()
user.increment_login_attempts()
user.describe()
user.reset_login_attempts()
user.describe()