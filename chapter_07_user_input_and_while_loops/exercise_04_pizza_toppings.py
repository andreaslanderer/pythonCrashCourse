prompt = "Please enter a topping you want to add to your pizza."
prompt += "\nOnce done, enter 'quit': "

while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"We will add {topping} to your pizza.")
