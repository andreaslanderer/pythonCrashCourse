from random import randint


class Dice:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(randint(1, self.sides))


dices = [
    Dice(),
    Dice(10),
    Dice(20)
]

for dice in dices:
    print(f"Rolling dice with {dice.sides} sides:")
    for i in range(1, 11):
        dice.roll_dice()
    print("---")
