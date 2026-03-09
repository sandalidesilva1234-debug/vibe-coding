def main():
    try:
        # Ask the user for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))
        
        # Collect expenses until 'done' is entered
        expenses = []
        while True:
            user_input = input("Enter an expense (or type 'done' to finish): ").strip().lower()
            if user_input == 'done':
                break
            try:
                expense = float(user_input)
                expenses.append(expense)
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")
            
        # Subtract expenses from total budget
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses
        
        # Display results
        print(f"\n--- Monthly Budget Summary ---")
        print(f"Total Budget:      ${total_budget:.2f}")
        print(f"Total Expenses:    ${total_expenses:.2f}")
        print(f"Remaining Balance: ${remaining_balance:.2f}")
        
        if remaining_balance < 500:
            print("Warning: Low Funds")
        
    except ValueError:
        print("Error: Please enter valid numeric values for budget and expenses.")

if __name__ == "__main__":
    main()
