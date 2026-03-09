  def main():
    # Task 01: Ask for total monthly budget
    try:
        budget_input = input("Enter your total monthly budget (LKR): ")
        total_budget = float(budget_input)
    except ValueError:
        print("Error: Please enter a valid numeric amount for the budget.")
        return

    remaining_balance = total_budget
    
    # Task 03: Enter expenses multiple times until "done"
    print("\nEnter your expenses one by one. Type 'done' when you are finished.")
    
    while True:
        entry = input("Enter expense amount (or type 'done'): ").strip().lower()
        
        if entry == 'done':
            break
        
        try:
            expense = float(entry)
            remaining_balance -= expense
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    # Task 01: Display remaining balance
    print(f"\n--- Summary ---")
    print(f"Total Budget: {total_budget:.2f} LKR")
    print(f"Remaining Balance: {remaining_balance:.2f} LKR")

    # Task 02: Add Warning Message
    if remaining_balance < 500:
        print("Warning: Low Funds")

if __name__ == "__main__":
    main()
