while True:
    name = input("Enter student's name (or type 'Exit' to finish): ")
    
    # Check for 'Exit' specifically
    if name == 'Exit':
        print("Exiting program. Goodbye!")
        break
        
    try:
        mark1 = float(input("Enter mark for subject 1: "))
        mark2 = float(input("Enter mark for subject 2: "))
        mark3 = float(input("Enter mark for subject 3: "))

        average = (mark1 + mark2 + mark3) / 3

        print("-" * 30)
        print(f"Name   : {name}")
        print(f"Average: {average:.1f}")

        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        print(f"Grade  : {grade}")
        print("-" * 30 + "\n")
        
    except ValueError:
        print("\n[Error] Invalid input. Please enter numeric values for marks.\n")
