guests = ["Aaron", "Abraham", "Bart, ""Bill", "Conrad", "Dorothea"]
guests.pop()    # dis-invite Dorothea
guests.pop(0)   # dis-invite Aaron
guests.pop(1)   # dis-invite Bart

guests.remove("Conrad")
del guests[0]
print(f"Remaining guests: {guests}")
