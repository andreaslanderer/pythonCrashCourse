basic_foods = ("paprika", "zucchini", "onions", "beef", "chicken")
for food in basic_foods:
    print(f"We have enough {food.title()}.")

try:
    # noinspection PyTupleItemAssignment
    basic_foods[-2] = "pork"
except TypeError as error:
    print(f"Trying to re-assign a tuple's value leads to: {error}")

basic_foods = list(basic_foods)
basic_foods[-2] = "mushrooms"
basic_foods[-1] = "tofu"
[print(f"We have enough {b.title()}") for b in basic_foods]  # list comprehension
