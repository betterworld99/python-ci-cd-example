def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
