guests = ["Abraham", "Bill", "Conrad"]
print(f"We've sent invitations to the following guests: {guests[0]}, {guests[1]} and {guests[2]}")

guests.insert(0, "Aaron")
guests.insert(2, "Bart")
guests.append("Dorothea")
guest_list = f"{guests[0]}, {guests[1]}, {guests[2]}, {guests[3]}, {guests[4]} and {guests[5]}"
print(f"Now we expect these guests: {guest_list}")
