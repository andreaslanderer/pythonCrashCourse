from random import choice

lottery_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E']
my_ticket = ['2', 'A', '5', '7']
lotteries = 0
won = False
while not won:
    lotteries += 1
    score = 0
    played_ticket = my_ticket[:]
    print(f"Playing lottery no.: {lotteries}")
    for i in range(4):
        chosen_number = choice(lottery_numbers)
        print(chosen_number)
        if chosen_number in played_ticket:
            score += 1
            played_ticket.remove(chosen_number)
    if score == 4:
        won = True
        print("-> Congratulations! You won the lottery!")
    else:
        print(f"-> You missed {4 - score} number(s)!")
