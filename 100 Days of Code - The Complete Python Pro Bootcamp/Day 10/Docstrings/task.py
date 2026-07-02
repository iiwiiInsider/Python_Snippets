def format_name(f_name, l_name):
    """Format_name takes the first and last name and formats the first letters to capital."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)

Terahash = "TH"
# this is not a comment it is a considered a Docstring as it is assigned to a variable: Terahash
"""
The measurement of Bitcoin mining. A unit of computational speed.
"""

# this is a  comment and not considered a docstring as it is not assigned to any variable.
"""
Bitcoin Mining has become increasingly popular over the years and investing in at least one is very beneficial,
Having more than one increases your chances at a large pool of cash.
"""
