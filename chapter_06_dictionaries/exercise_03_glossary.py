description_pikachu = ("An Electric-type Pokémon, known for its yellow fur with brown stripes on its back" +
                       "and its ability to generate electricity which it releases through its red cheeks.")
description_meowth = ("A small, feline Pokémon known for its distinct long, curled tail and the charm " +
                      "on its forehead, often seen attempting to speak human language.")
description_mew = ("A Psychic-type Mythical Pokémon with a playful and curious nature, known for its ability " +
                   "to learn any move and its genetic composition that encompasses the DNA of all " +
                   "existing Pokémon species.")
description_celebi = ("A Psychic/Grass-type Mythical Pokémon known as the 'Voice of the Forest', " +
                      "with the ability to travel through time and bring fertility to barren lands.")
# noinspection SqlDialectInspection,SqlNoDataSourceInspection
description_lugia = ("A Psychic/Flying-type Legendary Pokémon known as the Guardian of the Seas, " +
                     "with impressive wings that can cause storms and the ability to calm raging storms as well.")
glossary = {
    "pikachu": description_pikachu,
    "meowth": description_meowth,
    "mew": description_mew,
    "lugia": description_lugia,
    "celebi": description_celebi,
}

print(f"Pokemon    : Celebi")
print(f"Description: {glossary['celebi']}\n")
print(f"Pokemon    : Lugia")
print(f"Description: {glossary['lugia']}\n")
print(f"Pokemon    : Mew")
print(f"Description: {glossary['mew']}\n")
print(f"Pokemon    : Meowth")
print(f"Description: {glossary['meowth']}\n")
print(f"Pokemon    : Pikachu")
print(f"Description: {glossary['pikachu']}\n")

