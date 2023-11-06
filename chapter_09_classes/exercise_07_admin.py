
class User:

    def __init__(self, user_name, first_name, last_name):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name

    def user_info(self):
        print(f"User: {self.user_name}")
        print(f"\tFirst Name: {self.first_name.title()}")
        print(f"\tLast Name : {self.last_name.title()}")


class Admin(User):

    def __init__(self, user_name, first_name, last_name, *privileges):
        super().__init__(user_name, first_name, last_name)
        self.privileges = privileges

    def user_info(self):
        super().user_info()
        print(f"\tPrivileges: ")
        [print(f"\t- {p.upper()}") for p in self.privileges]


admin = Admin("andreas.landerer@gmail.com",
              "andreas",
              "landerer",
              "create", "read", "update", "delete")
admin.user_info()
