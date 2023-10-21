guests = ["Abraham", "Benjamin", "Conrad"]
print(f"We have invited the following guests: {guests[0]}, {guests[1]} and {guests[2]}")
print(f"Unfortunately, {guests[1]} can't make it")

guests[1] = "Bill"
print(f"A new set of invites has been sent to: {guests[0]}, {guests[1]} and {guests[2]}")
