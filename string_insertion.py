def insert_in_middle(original_string, insert_string):
    # Calculate the index to insert the string in the middle
    middle_index = len(original_string) // 2
    
    # Insert the string in the middle
    result_string = original_string[:middle_index] + insert_string + original_string[middle_index:]
    # here we use string slicing technique
    
    return result_string

# Test the function
original_string = input("Enter the original string: ")
insert_string = input("Enter the string to insert: ")

result = insert_in_middle(original_string, insert_string)
print("Resulting string:", result)


