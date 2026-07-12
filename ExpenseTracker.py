# Expense Tracker
# Author: Aldrich Martinez
# Language: Python

#Description: This is a simple expense tracker program that allows users to input their expenses from the program into a csv file.

#Features:
# 1. Add Expense: Users can input ther expenses by providing its category, amount, pieces, and descriprtion. 
#  - It also calculates the total amount of the expense by multiplying the amount and pieces.
# 2. View Expenses: Users can view all the expenses they have entered in the program. 
# 3. Search by Category: Users can search for their expenses by category.
# 4. Total Expenses: Shows the total expenses.
# 5. Category Summary: Shows the total expenses per category.
# 6. Delete Expense: Users can delete an expense by providing the expense number.

#CSV Format:
# The expenses are stored in a CSV file named "Expenses.csv" which has the given columns:
# Date, Category, Amoumt, Pieces, Total Amount, Description

import csv
import os
from datetime import datetime

fileName = "Expenses.csv"

def initialize_file():
    expected_header = ["Date", "Category", "Amount", "Pieces", "Total Amount", "Description"]

    if not os.path.exists(fileName):
        with open(fileName, mode='w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(expected_header)
        return

    with open(fileName, mode='r', newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        rows = list(reader)

    if header != expected_header:
        with open(fileName, mode='w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(expected_header)
            writer.writerows(rows)
        print(f"{fileName} header was corrected")

def add_expense():
    print("\n Add a New Expense \n")
    category = input("Input category expense: ")

    while True:
        try:
            amount = float(input("Input amount expense: "))
            if amount <= 0:
                print("Amount must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid Input. Please try again.")

    while True:
        try:
            pieces = int(input("Input no. of pieces: "))
            if pieces <= 0:
                print("Pieces must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid Input. Please try again.")

    totalAmount = amount * pieces
    description = input("Input description: ")

    date = datetime.now().strftime("%Y-%m-%d")
    with open(fileName, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, pieces, totalAmount, description])

    print("\n Expense added successfully \n")

def view_expenses():
    print("\n View Expenses \n")
    if not os.path.exists(fileName):
        print(f"{fileName} does not exist. Please add an expense first.")
        return

    with open(fileName, "r") as file:
        reader = csv.reader(file)
        
        next(reader)
        expense_number = 1
        found = False

        for row in reader:
            if len(row) < 6:
                continue
            found = True 

            print(f"Expense #{expense_number}")
            print(f"Date: {row[0]}")
            print(f"Category: {row[1]}")
            print(f"Amount: {row[2]}")
            print(f"Pieces: {row[3]}")
            print(f"Total Amount: {row[4]}")
            print(f"Description: {row[5]}")

            expense_number += 1
        if not found:
            print("No Expenses Found.")

def search_category():
    category = input("Enter Category to search: ").lower()

    found = False

    print("\n Search Results \n")

    with open(fileName, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) < 6:
                continue
            if row[1].lower() == category:
                found = True
                print(f"Date: {row[0]}")
                print(f"Category: {row[1]}")
                print(f"Amount: {row[2]}")
                print(f"Pieces: {row[3]}")
                print(f"Total Amount: {row[4]}")
                print(f"Description: {row[5]}")
                print("------------------------")

    if not found:
        print("No Category Match Found.")

def total_expenses():
    total = 0.0
    with open(fileName, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[4])

    print(f"\n Total Expenses: {total} \n")

def category_summary():
    summary = {}
    with open(fileName, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            category = row[1]
            total_amount = float(row[4])

            if category in summary:
                summary[category] += total_amount
            else:
                summary[category] = total_amount
    print("\n Category Summary \n")
    if len(summary) == 0:
        print("No Expenses Found.")
        return
    for category, total in summary.items():
        print(f"Category: {category}, Total Amount: {total}")

def delete_expense():
    view_expenses()
    expense_number = input("Enter the expense number to delete: ")

    try:
        expense_number = int(expense_number)
        if expense_number <= 0:
            print("Invalid expense number. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid expense number.")
        return

    with open(fileName, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if expense_number >= len(expenses):
        print("Expense number out of range. Please try again.")
        return

    del expenses[expense_number]

    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

    print("\n Expense deleted successfully \n")

def main():
    initialize_file()

    while True:
        print("\n Expense Tracker Menu \n")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Total Expenses")
        print("5. Category Summary")
        print("6. Delete Expense")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_category()
        elif choice == "4":
            total_expenses()
        elif choice == "5":
            category_summary()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            print("Exiting the program. Thank you")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



