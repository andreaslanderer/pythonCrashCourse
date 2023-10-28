poll = {
    "andreas": "kotlin",
    "daniel": "c++",
    "iris": "python",
    "julius": "c",
}

friends = {"daniel", "franziska", "iris", "julius"}

for friend in friends:
    if friend in poll.keys():
        print(f"Thank you, {friend.title()} for participating in the poll.")
    else:
        print(f"{friend.title()} could you please participate in the poll?")
