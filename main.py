import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n----- Expense List -----")

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No expense records found.")


def search_expense():
    keyword = input("Enter category to search: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if keyword.lower() in row[1].lower():
                print(row)
                found = True

    if not found:
        print("No matching expenses found.")


def total_expense():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[3])

    print(f"Total Expense: ₹{total:.2f}")


def main():

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

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            total_expense()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


main()