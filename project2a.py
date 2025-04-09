def main():
    numbers = []
    print("Enter five numbers:")

    for i in range(5):
        while True:
            try:
                num = float(input(f"Number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    average = sum(numbers) / len(numbers)
    print(f"\nThe average of the numbers is: {average}")

if __name__ == "__main__":
    main()