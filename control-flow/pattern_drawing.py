# pattern_drawing.py

def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1

if __name__ == "__main__":
    main()
