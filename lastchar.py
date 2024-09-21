def four_copies_of_last_two_chars(input_string):
    # Check if the input string has at least 2 characters
    if len(input_string) < 2:
        return "Error: Length must be at least 2"

    # Get the last two characters of the input string
    last_two_chars = input_string[-2:]

    # Create a new string by repeating the last two characters four times
    result_string = last_two_chars * 4

    return result_string

# Test the function
input_string = input("Enter a string (at least 2 characters): ")
result = four_copies_of_last_two_chars(input_string)
print("Result:", result)
