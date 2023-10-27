beverages = ["coca cola", "beer", "apple juice", "lemonade", "gin tonic"]

print("My favorite beverages are:")
for beverage in beverages[:3]:
    print(f"\t{beverage.title()}")

print("My favorite beverages are:")
[print(f"\t{b.title()}") for b in beverages[-3:]]  # list comprehension
