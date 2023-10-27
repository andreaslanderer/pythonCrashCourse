# noinspection PyListCreation
pokemon = ["Onyx", "Mew", "Bisasam", "Zapdos"]

# Add pokemon
pokemon.append("Pikachu")
pokemon.insert(0, "Mauzi")
pokemon.insert(3, "Lugia")

# Replace pokemon
pokemon[2] = "Mewto"

print(pokemon)

# Delete pokemon
del pokemon[0]
pokemon.pop()
pokemon.pop(1)
pokemon.remove("Bisasam")

print(pokemon)

# Sort pokemon
print(sorted(pokemon))
print(pokemon)
pokemon.sort()
print(pokemon)
pokemon.reverse()
print(pokemon)

