
class User:

    def __init__(self,
                 first_name,
                 last_name,
                 user_name,
                 email,
                 date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.date_of_birth = date_of_birth

    def describe(self):
        print(f"User: {self.user_name}")
        print(f"\tFirst Name   : {self.first_name.title()}")
        print(f"\tLast Name    : {self.last_name.title()}")
        print(f"\tEmail Address: {self.email}")
        print(f"\tDate of Birth: {self.date_of_birth}")
        print("---")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")


users = [
    User("andreas",
         "landerer",
         "alanderer",
         "andreas.landerer@gmail.com",
         "1983-02-11"),
    User("julius",
         "schneider",
         "jschneider",
         "julius.schneider@yahoo.com",
         "1993-06-01")
]

[u.describe() for u in users]
[u.greet_user() for u in users]
