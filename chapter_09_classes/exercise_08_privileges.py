
class Admin:

    def __init__(self, user_name, privileges):
        self.user_name = user_name
        self.privileges = privileges

    def user_info(self):
        print(f"User name : {self.user_name}")
        self.privileges.show_privileges()


class Privilege:

    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        privilege_string = ""
        for p in self.privileges:
            privilege_string += f"{p.upper()} "
        print(f"Privileges: {privilege_string}")


admin = Admin("andreas.landerer@gmail.com",
              Privilege("create", "read", "update", "delete"))
admin.user_info()
