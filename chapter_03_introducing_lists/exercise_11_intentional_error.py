empty_list = []
try:
    print(f"The first element of the empty list is set to {empty_list[0]}")
except IndexError as error:
    print(f"Trying to access a non-existing index leads the following error: {error}")
