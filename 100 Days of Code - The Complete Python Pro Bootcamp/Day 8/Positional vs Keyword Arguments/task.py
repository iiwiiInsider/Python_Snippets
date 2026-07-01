# function with more than 1 input:
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#  Positional Arguments are less accurate and can be confusing if the order is not correct
greet_with("Kyle Blackburn", "14 Stork Road")

# Keyword arguments associates the data more accurately.
greet_with(name="Kyle Blackburn", location="The Himalayan Salt caves")