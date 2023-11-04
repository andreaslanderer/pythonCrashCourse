
def make_shirt(text, size="large"):
    """This function makes shirts of a given size displaying a chosen text"""
    print(f"Your {size}-sized shirt with the text '{text}' is in production.")


make_shirt("I love Python")
make_shirt("I love Python", "medium")
make_shirt(size="small", text="Java rocks!")
