class Expense: 
    def __init__(self,title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        title = input("Enter expense title ")
        amount = float(input("Enter the amount: "))
        category = input("Enter the category")

        expense = self.expenses(title, amount, category )

        self.expenses.append(expense)
        print("Expenses added successfully")

    def view_exapnses(self):
        if not self.expenses:
            print("No expenses found")
            return
        
        for expense in self.expenses:
            print("\n Title: ", self.title)
            print("Amount: ", self.amount)
            print("Category: ", self.category)

    def calculate_expenses(self):
        total = 0
        for expense in self.expenses:
            total = total + expense.amount
            print("Total expenses: ", total)

    def search_by_category(self):
        category = input("Enter category to search: ")
        found = False

        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                print("\n Title: ", expense.title)
                print("Amount: ", self.amount)
                print("Category: ", self.category)

                found = True

            if not found:
                print("There is no such category")

tracker = ExpenseTracker()

while True:
    print("\n===== EXPENSE TRACKER =====")

    print("1. Add Expense")

    print("2. View Expenses")

    print("3. Calculate Total")

    print("4. Search by Category")

    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        tracker.add_expense()

    elif choice == "2":

        tracker.view_expenses()

    elif choice == "3":

        tracker.calculate_total()

    elif choice == "4":

        tracker.search_by_category()

    elif choice == "5":

        print("Exiting Expense Tracker...")

        break

    else:

        print("Invalid choice. Please try again.")




