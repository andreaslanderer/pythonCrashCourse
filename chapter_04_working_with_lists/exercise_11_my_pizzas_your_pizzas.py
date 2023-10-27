my_pizzas = ["Salami", "Napoli", "Hawaii"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("Bolognese")
friend_pizzas.append("Verdure")

print("My favorite pizzas are:")
[print(f"\t{p}") for p in my_pizzas]  # list comprehension

print("My friend's favorite pizzas are:")
[print(f"\t{p}") for p in friend_pizzas]  # list comprehension
