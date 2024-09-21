my_list = [1, 2, 3, 4, 5]


# Open a file in write mode
with open('output.txt', 'w') as file:
    # Iterate through the list and write each element to the file
    for item in my_list:
        file.write(str(item) + '\n')
