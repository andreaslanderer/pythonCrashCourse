from admin import Admin, Privilege

admin_rights = Privilege("create", "read", "update", "delete")
admin_user = Admin("andreas.landerer@gmail.com", admin_rights)
admin_user.user_info()
