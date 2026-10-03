# Universal Number System Converter
# Binary, Decimal, Octal and Hexadecimal

DIGITS = "0123456789ABCDEF"


def to_decimal(number, base):
    """Convert any base number to decimal."""

    number = number.upper()

    value = 0

    for digit in number:
        value = value * base + DIGITS.index(digit)

    return value


def from_decimal(number, base):
    """Convert decimal number to another base."""

    if number == 0:
        return "0"

    result = ""

    while number > 0:
        remainder = number % base
        result = DIGITS[remainder] + result
        number = number // base

    return result


def convert_number(number, source_base, target_base):

    # First convert to decimal
    decimal_number = to_decimal(number, source_base)

    # Then convert decimal to target base
    result = from_decimal(decimal_number, target_base)

    return result


# -----------------------------
# Main Program
# -----------------------------

print("=" * 50)
print("       NUMBER SYSTEM CONVERTER")
print("=" * 50)

print("""
1. Binary
2. Decimal
3. Octal
4. Hexadecimal
""")

source_choice = int(input("Enter the input number system (1-4): "))

number = input("Enter the number: ").strip()

print("""
1. Binary
2. Decimal
3. Octal
4. Hexadecimal
5. All
""")

target_choice = int(input("Enter the output number system (1-5): "))


# Map choices to bases
base_map = {
    1: 2,
    2: 10,
    3: 8,
    4: 16
}

name_map = {
    1: "Binary",
    2: "Decimal",
    3: "Octal",
    4: "Hexadecimal"
}


try:

    source_base = base_map[source_choice]

    # Convert to all number systems
    if target_choice == 5:

        decimal_number = to_decimal(
            number,
            source_base
        )

        print("\n" + "=" * 40)
        print("CONVERSION RESULTS")
        print("=" * 40)

        for choice in range(1, 5):

            target_base = base_map[choice]

            result = from_decimal(
                decimal_number,
                target_base
            )

            print(
                f"{name_map[choice]:12} : {result}"
            )

    # Convert to selected number system
    elif target_choice in base_map:

        target_base = base_map[target_choice]

        result = convert_number(
            number,
            source_base,
            target_base
        )

        print("\n" + "=" * 40)
        print("RESULT")
        print("=" * 40)

        print(
            f"{number} ({name_map[source_choice]}) "
            f"= {result} ({name_map[target_choice]})"
        )

    else:
        print("Invalid output choice.")

except ValueError:
    print("\nError: Please enter a valid number.")

except KeyError:
    print("\nError: Please select a number system from 1-4.")
