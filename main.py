import csv
from datetime import datetime

# Name of the CSV file used to store expense records
FILE_NAME = "expenses.csv"


# Add a new expense record to the CSV file
def add_expense():
    # Get the current date automatically
    date = datetime.now().strftime("%Y-%m-%d")

    # Get expense details from the user
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        # Convert the entered amount into a number
        amount = float(input("Enter amount: "))
    except ValueError:
        # Handle invalid amount input
        print("Invalid amount!")
        return

    # Open the CSV file in append mode and save the expense
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


# Display all saved expense records
def view_expenses():
    try:
        # Read expense records from the CSV file
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n----- Expense List -----")

            # Display each expense record
            for row in reader:
                print(row)

    # Handle the case when the expense file does not exist
    except FileNotFoundError:
        print("No expense records found.")


# Search for expenses using a category keyword
def search_expense():
    keyword = input("Enter category to search: ")

    # Track whether a matching expense was found
    found = False

    # Read the stored expense records
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        # Check each record for the searched category
        for row in reader:
            if keyword.lower() in row[1].lower():
                print(row)
                found = True

    # Display a message if no matching record was found
    if not found:
        print("No matching expenses found.")


# Calculate and display the total expense amount
def total_expense():
    total = 0

    # Read expense records from the CSV file
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        # Skip the first row
        next(reader)

        # Add each expense amount to the total
        for row in reader:
            total += float(row[3])

    print(f"Total Expense: ₹{total:.2f}")


# Display the main menu and handle user choices
def main():

    # Keep the application running until the user chooses Exit
    while True:
        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. View Total Expense")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Add a new expense
        if choice == "1":
            add_expense()

        # View all expenses
        elif choice == "2":
            view_expenses()

        # Search expenses by category
        elif choice == "3":
            search_expense()

        # Calculate total expenses
        elif choice == "4":
            total_expense()

        # Exit the application
        elif choice == "5":
            print("Thank you!")
            break

        # Handle invalid menu choices
        else:
            print("Invalid choice!")


# Start the Expense Tracker application
main()
