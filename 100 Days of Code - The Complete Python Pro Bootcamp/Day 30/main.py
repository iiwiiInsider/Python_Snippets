# #FileNotFound
#
# try:
#     file = open("a_exisiting_file.txt",)
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
#
# except FileNotFoundError:
#     file = open("a_exisiting_file.txt","w")
#     file.write("This is a new file created because the original file was not found.")
#
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist in the dictionary.")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     raise TypeError("This is a custom error message due to no logic found in this program.")

height = float(input("Height: "))
if height > 3:
    raise ValueError("Human Height should not be greater than 3")
height = float(input("Height: "))
weight = float(input("Weight: "))

bmi = weight / (height ** 2)
print(bmi)
