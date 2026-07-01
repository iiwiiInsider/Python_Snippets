programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Function"])   # prints the value of the key "Function" in the variable programming_dictionary.

programming_dictionary["Loop"] = "The action of doing something over and over again." # adds a new key value pair to the dictionary.

print(programming_dictionary) # prints the previous 2 keys and the newly added Key values in the variable programming_dictionary.

empty_dictionary = {}

#Wipe an existing dictionary

programming_dictionary = {}
print(programming_dictionary) # prints an empty dictionary since it has been wiped.

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A mistake in the code that causes the program to behave unexpectedly." # updates the value of the key "Bug" in the dictionary.

print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key) # prints the keys in the dictionary.
    print(programming_dictionary[key]) # prints the values of the keys in the dictionary.