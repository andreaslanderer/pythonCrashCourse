"""This module contains the User class"""


class User:

    def __init__(self, user_name):
        self.user_name = user_name

    def user_info(self):
        print(f"User")
        print(f"\t- User Name : {self.user_name}")
