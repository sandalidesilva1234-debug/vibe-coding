def main():
    # Ask for student's name
    name = input("Enter student's name: ")

    # Ask for 3 subject marks
    try:
        mark1 = float(input("Enter mark for Subject 1: "))
        mark2 = float(input("Enter mark for Subject 2: "))
        mark3 = float(input("Enter mark for Subject 3: "))

        # Calculate the average
        average = (mark1 + mark2 + mark3) / 3

        print(f"\nStudent: {name}")
        print(f"Average Mark: {average:.2f}")

        # Determine and display Pass/Fail status
        if average >= 40:
            print("Status: Pass")
        else:
            print("Status: Fail")

    except ValueError:
        print("Invalid input. Please enter numeric values for marks.")

if __name__ == "__main__":
    main()
