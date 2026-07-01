# ASCII Art Banner
print(r"""

            C A E S A R ' S   C I P H E R
            
""")


alphabet = "abcdefghijklmnopqrstuvwxyz"

# Validate direction input
while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    if direction in ["encode", "decode"]:
        break
    print("Invalid input. Please type 'encode' or 'decode'.")

# Validate message input (letters + spaces only)
while True:
    text = input("Type your message:\n")
    if all(char.isalpha() or char.isspace() for char in text):
        break
    print("Message may only contain letters and spaces.")

# Validate shift input
while True:
    try:
        shift = int(input("Type the shift number:\n"))
        break
    except ValueError:
        print("Shift must be a valid number.")

# Normalize shift
shift = shift % len(alphabet)

def caesar(original_text, shift_amount, mode):
    result = ""
    for char in original_text:
        if char.isalpha():
            is_upper = char.isupper()
            base = alphabet.upper() if is_upper else alphabet

            pos = base.index(char)
            if mode == "encode":
                new_pos = (pos + shift_amount) % 26
            else:
                new_pos = (pos - shift_amount) % 26

            result += base[new_pos]
        else:
            result += char
    return result

output = caesar(text, shift, direction)

print(f"\nHere is the {direction}d result: {output}")
