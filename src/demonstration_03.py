"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt: str) -> int:
    # Your code here
    if txt.isnumberic() is True;    
    converted_int = int(txt)
    return converted_int

    else:
        return f"'(txt)' is not a valid number"

print(string_int("1000"))

