"""This module contains the Admin in Privilege classes"""

from user import User


class Privilege:

    def __init__(self, *privileges):
        self.privileges = privileges


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
