"""This module contains all admin related files"""


class User:

    def __init__(self, user_name):
        self.user_name = user_name

    def user_info(self):
        print(f"User")
        print(f"\t- User Name : {self.user_name}")


class Admin(User):

    def __init__(self, user_name, privilege):
        super().__init__(user_name)
        self.privilege = privilege

    def user_info(self):
        super().user_info()
        privilege_string = ""
        for p in self.privilege.privileges:
            privilege_string += f"{p.upper()} "
        print(f"\t- Privileges: {privilege_string}")


class Privilege:

    def __init__(self, *privileges):
        self.privileges = privileges
