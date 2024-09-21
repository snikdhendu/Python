import sys

# Check if there are exactly 3 command line arguments
if len(sys.argv) != 4:
    print("Invalid input. Usage: <number> <operator> <number>")
else:
    try:
        first_operand = float(sys.argv[1])
        operator = sys.argv[2]
        second_operand = float(sys.argv[3])

        if operator == '+':
            result = first_operand + second_operand
        elif operator == '-':
            result = first_operand - second_operand
        else:
            print("Invalid operator. Only '+' and '-' are supported.")
            sys.exit(1)

        print("Result:", result)

    except ValueError:
        print("Invalid number format. Numbers must be in decimal format.")
    except Exception as e:
        print("An unexpected error occurred:", e)
