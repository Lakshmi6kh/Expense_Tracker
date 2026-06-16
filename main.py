from expense_tracker import add_expenses,view_expenses,view_total,filter_category,load_expenses,save_expense
print("welcome to Expense tracker!")
print("1.Add Expense\n2.View Expense\n3.View Total\n4.Filter by category\n5.Exit")
while True:
    choice=int(input("Enter your choice :"))
    if(choice==1):
        expenses=load_expenses()
        add_expenses()
    elif(choice==2):
        expenses=load_expenses()
        view_expenses(expenses)
    elif(choice==3):
        expenses=load_expenses()
        view_total(expenses)
    elif(choice==4):
        expenses=load_expenses()
        filter_category(expenses)
    elif(choice==5):
        exit()
    