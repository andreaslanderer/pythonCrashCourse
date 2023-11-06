from random import choice

lottery_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E']

chosen_numbers = []
for i in range(4):
    chosen_numbers.append(choice(lottery_numbers))
print(f"Any ticket containing the following numbers have won a prize: {chosen_numbers}")
