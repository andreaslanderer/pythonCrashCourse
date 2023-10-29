prompt = "Enter your age and we will calculate the ticket price for you."
prompt += "\nEnter 'quit' when you're done: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        else:
            price = 15
    print(f"Your ticket is USD {price}.")
