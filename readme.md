Expense Tracker

A simple command-line Expense Tracker built with Python. This application allows users to record, view, and analyze their expenses using a CSV file for data storage.

Features
Add new expenses
View all recorded expenses
Calculate total expenses
Filter expenses by category
Store data permanently in a CSV file
Project Structure
expense_tracker/
 main.py
 expense_tracker.py
 expenses.csv
 README.md
Technologies Used
Python 3
CSV Module (built-in)
Data Format

Expenses are stored in expenses.csv using the following structure:

date,amount,category,description
2026-06-16,250,Food,Lunch
2026-06-16,500,Travel,Bus Ticket
Usage

Run the application:

python main.py

Example menu:

===== Expense Tracker =====

1. Add Expense
2. View Expenses
3. Calculate Total Expenses
4. Filter Expenses By Category
5. Exit
Example Expense
{
    "date": "2026-06-16",
    "amount": 250,
    "category": "Food",
    "description": "Lunch"
}

This project demonstrates:

Python functions
Lists and dictionaries
File handling
CSV processing
Loops and conditionals
Modular programming