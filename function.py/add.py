def _sum(*args):
    return sum(args)

# Test the function
n = int(input("Enter the number of integers: "))
numbers = [int(input(f"Enter integer {i + 1}: ")) for i in range(n)]

result = _sum(numbers)
print(f"Sum of the integers: {result}")