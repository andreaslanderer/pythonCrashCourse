
def send_messages(messages):
    """Sending messages and returns list of successfully sent messages"""
    sent_messages = []
    for message in messages:
        print(f"Sending message: '{message}'")
        sent_messages.append(message)
    return sent_messages


messages_to_be_sent = [
    "3 + 5 = 8",
    "The cake is a lie",
    "Welcome to the jungle"
]
messages_sent = send_messages(messages_to_be_sent)
print(messages_sent)
