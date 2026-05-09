import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


# ---------- CREATE CSV FILE ----------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Description", "Date"])


# ---------- ADD EXPENSE ----------
def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()
        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, description, date])

        print("\nExpense added successfully!")

    except ValueError:
        print("Invalid amount entered.")


# ---------- VIEW EXPENSES ----------
def view_expenses():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No expenses found.")
                return

            print("\n===== ALL EXPENSES =====\n")

            for row in rows[1:]:
                print(
                    f"Date: {row[3]} | "
                    f"Amount: ₹{row[0]} | "
                    f"Category: {row[1]} | "
                    f"Description: {row[2]}"
                )

    except FileNotFoundError:
        print("Expense file not found.")


# ---------- MONTHLY SUMMARY ----------
def monthly_summary():
    month = input("Enter month (YYYY-MM): ")

    total = 0

    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Date"].startswith(month):
                    total += float(row["Amount"])

        print(f"\nTotal expense for {month}: ₹{total}")

    except:
        print("Error reading file.")


# ---------- CATEGORY BREAKDOWN ----------
def category_breakdown():
    category_totals = {}

    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                category = row["Category"]
                amount = float(row["Amount"])

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

        if not category_totals:
            print("No expense data found.")
            return None

        print("\n===== CATEGORY BREAKDOWN =====")

        for category, total in category_totals.items():
            print(f"{category}: ₹{total}")

        return category_totals

    except:
        print("Error reading data.")
        return None


# ---------- HIGHEST SPENDING CATEGORY ----------
def highest_spending_category():
    data = category_breakdown()

    if data:
        highest = max(data, key=data.get)
        print(f"\nHighest spending category: {highest}")


# ---------- PIE CHART ----------
def show_pie_chart():
    data = category_breakdown()

    if data:
        labels = data.keys()
        values = data.values()

        plt.figure(figsize=(7, 7))
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title("Expense Distribution")
        plt.show()


# ---------- MAIN MENU ----------
def main():

    initialize_file()

    while True:

        print("\n====== SMART EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Breakdown")
        print("5. Highest Spending Category")
        print("6. Show Pie Chart")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            monthly_summary()

        elif choice == "4":
            category_breakdown()

        elif choice == "5":
            highest_spending_category()

        elif choice == "6":
            show_pie_chart()

        elif choice == "7":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


# ---------- RUN PROGRAM ----------
if __name__ == "__main__":
    main()