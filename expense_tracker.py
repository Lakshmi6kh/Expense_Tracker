import csv

def add_expenses():
        date=input("Enter the date : ")
        amt=int(input("Enter the amount spent : "))
        category=input("Enter the category : ")
        description=input("enter the decription : ")
        expense={
                "date" :date,
                "amount":amt,
                "category":category,
                "description":description
        }
        save_expense(expense)
def view_expenses(expenses):
        for expense in expenses:
                print(expense)
def view_total(expenses):
        total=0
        for expense in expenses:
                total+=expense["amount"]
        print("The total amount spent is : ",total)
def filter_category(expenses):
        category=input("Enter a category : ").lower()
        filtered=[]
        for expense in expenses:
                if expense["category"].lower()==category:
                        filtered.append(expense)
        print(filtered)
def save_expense(expense):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            expense["date"],
            expense["amount"],
            expense["category"],
            expense["description"]
        ])
def load_expenses():
    expenses = []

    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append({
                "date": row["date"],
                "amount": float(row["amount"]),
                "category": row["category"],
                "description": row["description"]
            })

    return expenses