def convert_to_uppercase(input_str):
    return input_str.upper()
def convert_to_uppercase(input_str):
    """
    Converts the input string to uppercase.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string with all uppercase letters.
    """
    return input_str.upper()

def capitalize_first_letters(input_str):
    """
    Capitalizes the first letter of each word in the input string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The input string with the first letter of each word capitalized.
    """
    words = input_str.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)