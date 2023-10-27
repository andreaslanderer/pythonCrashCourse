current_users = ["andreas", "daniel", "Franziska", "iris", "Julius"]
new_users = ["Ferdinand", "franziska", "Markus", "nick", "Tim"]

current_users_lower_case = []
for user in current_users:
    current_users_lower_case.append(user.lower())

for new_user in new_users:
    if new_user not in current_users_lower_case:
        print(f"The name {new_user.lower()} is still available")
    else:
        print(f"The user {new_user.lower()} is already in use")
