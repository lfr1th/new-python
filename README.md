Expense Tracker

Author: Aldrich Martinez
Language: Python


Description

A simple command-line expense tracker that lets you log, view, search, and manage your expenses. All data is saved to a CSV file (Expenses.csv) so your records persist between sessions.


Features

1. Add Expense

Log a new expense by entering:


Category — e.g. Food, Transport, Utilities
Amount — unit price of the item
Pieces — quantity purchased
Description — brief note about the expense


The program automatically calculates the Total Amount (Amount × Pieces) and records the current Date.

2. View Expenses

Displays all recorded expenses in a formatted list showing the expense number, date, category, amount, pieces, total amount, and description.

3. Search by Category

Filter and display only the expenses that match a specific category name.

4. Total Expenses

Shows the grand total of all expenses recorded across all categories.

5. Category Summary

Shows a breakdown of total spending per category, useful for identifying where most of your money goes.

6. Delete Expense

Remove a specific expense by entering its expense number from the list.


CSV Format

Expenses are stored in a file named Expenses.csv with the following columns:

ColumnDescriptionDateDate the expense was recordedCategoryType/category of the expenseAmountUnit price of the itemPiecesQuantity purchasedTotal AmountCalculated as Amount × PiecesDescriptionBrief note about the expense

The file is created automatically on first use if it does not already exist.


How to Run

bashpython expense_tracker.py

No external libraries required — uses only Python's built-in csv and datetime modules.
