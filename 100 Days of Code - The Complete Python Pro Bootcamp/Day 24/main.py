# main.py

# File paths based on your project structure
LETTER_TEMPLATE_PATH = "./Input/Letters/starting_letter.txt"
NAMES_PATH = "./Input/Names/invited_names.txt"
OUTPUT_DIR = "./Output/ReadyToSend/"

def main():
    # Read the letter template
    with open(LETTER_TEMPLATE_PATH, "r") as letter_file:
        letter_template = letter_file.read()

    # Read the list of names
    with open(NAMES_PATH, "r") as names_file:
        names = names_file.readlines()

    # Create a personalized letter for each name
    for name in names:
        clean_name = name.strip()  # Remove newline characters

        # Replace placeholder
        personalized_letter = letter_template.replace("[name]", clean_name)

        # Save the new letter
        output_path = f"{OUTPUT_DIR}letter_for_{clean_name}.txt"
        with open(output_path, "w") as output_file:
            output_file.write(personalized_letter)

        print(f"Created letter for {clean_name}")

if __name__ == "__main__":
    main()
