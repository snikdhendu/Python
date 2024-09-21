# Initialize empty lists
date_of_birth_list = []
day_list = []
month_list = []
year_list = []

# Input the number of students
N = int(input("Enter the number of students: "))

# Read date of birth for each student and store in the list
for i in range(N):
    date_of_birth = input(f"Enter the date of birth for student {i + 1} (dd-mm-yyyy): ")
    date_of_birth_list.append(date_of_birth)

# Sort the list in ascending order
date_of_birth_list.sort()

# Extract day, month, and year from each date and store in separate lists
for dob in date_of_birth_list:
    day, month, year = dob.split('-')
    day_list.append(day)
    month_list.append(month)
    year_list.append(year)

# Print the lists
print("Date of Birth List:", date_of_birth_list)
print("Day List:", day_list)
print("Month List:", month_list)
print("Year List:", year_list)
