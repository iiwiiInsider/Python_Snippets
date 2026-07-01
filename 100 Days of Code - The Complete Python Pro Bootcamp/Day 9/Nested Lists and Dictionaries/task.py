capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lyon", "Marseille"], # Nested List Inside a Dictionary
    "Germany": ["Berlin", "Hamburg", "Munich"], # Nested List Inside a Dictionary
}

# Print Lille indexing the second value in France Key from dictionary travel_log

print(travel_log["France"][1])

nested_list = ["A","B","C","D",["E","F","G","H"]]

# Print the value "G" from the nested list
print(nested_list[4][2])
#                 ^
#                 |
# Index 4 is the nested list & within the list "G" is indexed at 2.


# Nesting a dictionary in a dictionary and a nested list
travel_log2 = {
    "France": {
        "num_times_visited": 2,
        "cities_visited": ["Paris", "Lyon", "Marseille"]
    },
    "Germany": {
        "num_times_visited": 3,
        "cities_visited": ["Berlin", "Hamburg", "Munich"]
    },
}

# Printing Hamburg from the nested dictionary and list travel_log2

print(travel_log2["Germany"]["cities_visited"][1])