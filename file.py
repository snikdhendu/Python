def temp_convert(var):
    try:
        return int(var)
    except (ValueError, TypeError) as e:
        print("The argument does not contain numbers\n", e)

# Call above function here.
temp_convert("xyz")
