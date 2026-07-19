# nato_phonetic_no_output.py
# Requires: pandas
# Install with: pip install pandas

import pandas as pd

# Given student_dict example (kept for data, but no printing)
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# (No output — removed print statements)
for (key, value) in student_dict.items():
    # Access key and value (kept for potential logic; no printing)
    _ = (key, value)  # placeholder to show we intentionally access them

# Create a DataFrame from the dictionary
student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row (no printing)
    _ = (index, row)  # placeholder to show we intentionally access them

# -------------------------
# TODO 1: Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# -------------------------

# Load the NATO phonetic CSV into a DataFrame
nato_csv = "nato_phonetic_alphabet.csv"
nato_df = pd.read_csv(nato_csv)

# Build the dictionary mapping single uppercase letters to code words
phonetic_dict = {row.letter.upper(): row.code for (_, row) in nato_df.iterrows()}

# -------------------------
# TODO 2: Create a list of the phonetic code words from a word that the user inputs.
# -------------------------

def word_to_phonetic(word: str, mapping: dict) -> list:
    """
    Convert a word into a list of NATO phonetic code words.
    Non-alphabetic characters are ignored.
    """
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")
    result = []
    for ch in word.upper():
        if ch.isalpha():
            if ch in mapping:
                result.append(mapping[ch])
            else:
                raise ValueError(f"No phonetic mapping for character: {ch}")
        else:
            continue
    return result

def main():
    # Only prompt and print the phonetic conversion when the user explicitly runs the conversion.
    user_input = input("Enter a word to convert to NATO phonetic code (or press Enter to exit): ").strip()
    if not user_input:
        # Exit silently without printing any other runtime info
        return

    try:
        phonetic_list = word_to_phonetic(user_input, phonetic_dict)
        # Single, intentional output: the conversion result
        print(f"Phonetic conversion for '{user_input}': {phonetic_list}")
    except Exception as e:
        # Print only the error message if conversion fails
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
