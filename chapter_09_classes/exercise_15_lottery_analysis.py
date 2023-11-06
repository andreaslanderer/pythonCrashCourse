from random import choice

lottery_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E']
my_ticket = ['2', 'A', '5', '7']
lotteries = 0
won = False
while not won:
    lotteries += 1
    print(f"Playing lottery no.: {lotteries}")
    my_ticket_copy = my_ticket[:]
    for i in range(4):
        chosen_number = choice(lottery_numbers)
        try:
            my_ticket_copy.remove(chosen_number)
        except ValueError:
            break
    if len(my_ticket_copy) == 0:
        won = True
        print("-> Congratulations! You won the lottery!")
    else:
        print(f"-> You missed {len(my_ticket_copy)} numbers!")
