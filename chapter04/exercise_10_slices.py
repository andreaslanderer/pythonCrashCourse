pokemon = ["Pikachu", "Mew", "Mauzi", "Mewto", "Lugia"]

print("The first three pokemon in the list are:")
[print(f"\t{p}") for p in pokemon[:3]]  # list comprehension

print("Three pokemon from the middle of the list are:")
[print(f"\t{p}") for p in pokemon[1:4]]  # list comprehension

print("The last three pokemon in the list are:")
[print(f"\t{p}") for p in pokemon[-3:]]  # list comprehension
