
def archive_messages(messages):
    """Prints and archives messages"""
    while messages:
        message = messages.pop(0)
        print(f"Archived message: '{message}'")


my_messages = ["Hello", "beautiful", "world"]
archive_messages(my_messages[:])
print(my_messages)
