# Expense tracker
# Expense class to handle individual expenses

from datetime import date

class Expense:
    def __init__(self, expense_amount: float, expense_description: str, date: date):
        self.expense_amount = expense_amount
        self.expense_description = expense_description
        self.date = date

    def edit_expense(self, expense_amount: float, expense_description: str, date: date):
        if expense_amount is not None:
            if expense_amount > 0:
                self.amount = expense_amount
            else:
                print("Amount must be positive")
        if expense_description is not None:
            self.description = expense_description
        if date is not None:
            self.date = date

    def __str__(self):
        return f"Amount: ₦{self.expense_amount}, Description: {self.expense_description}, Date: {self.date}"

class Category:
    def __init__(self, category_name):
        self.category_name = category_name

    def __str__(self):
        return f"Category Name: {self.category_name}"
    
class Budget:
    def __init__(self, budget_amount: float):
        self.budget_amount = budget_amount

    def add_budget(self, amount: float):
        if amount > 0:
            self.budget_amount += amount
        else:
            return f"Amount must be positive"
        
    def deduct_budget(self, amount: float):
        if amount > 0:
            if amount <= self.budget_amount:
                self.budget_amount -= amount
            else:
                print("Insufficient funds")
        else:
            print("Amount must be positive")

    def __str__(self):
        return f"Budget: ₦{self.budget_amount:.2f}"

class ExpenseManager:
    def __init__(self, budget: Budget, expenses = None, categories = None, total_expense = 0):
        if expenses is None:
            expenses = []
        if categories is None:
            categories = []
        self.budget = budget
        self.expenses = expenses
        self.categories = categories
        self.total_expense = total_expense

    def add_expense(self, expense: Expense):
        if expense not in self.expenses:
            self.expenses.append(expense)
            self.total_expense += expense.expense_amount
            self.budget.deduct_budget(expense.expense_amount)
        else:
            print(f"Expense '{expense}' already exists")

    def add_category(self, category):
        if category not in self.categories: 
            self.categories.append(category)
        else:
            raise(f"Category '{category.category_name}' already exists.")

    def remove_expense(self, expense: Expense):
        try:    
            self.expenses.remove(expense)
            self.total_expense -= expense.expense_amount
            self.budget.add_budget(expense.expense_amount)
        except ValueError:
            raise(f"Expense '{expense}' not found")

    def remove_category(self, category):
        try:
            self.categories.remove(category)
        except ValueError:
            raise(f"Category '{category.category_name}' not found")

    def display_expense(self):
        for expense in self.expenses:
            print(expense)

    def display_category(self):
        for category in self.categories:
            print(category)

    def display_total_expense(self):
        print(f"Total Expense: ₦{self.total_expense:.2f}")
 

# Example usage:
budget = Budget(1000)
expense_manager = ExpenseManager(budget)

expense1 = Expense(25, 'Groceries', date.today())
expense2 = Expense(79, 'Car Repair', date.today())

expense_manager.add_expense(expense1)
expense_manager.add_expense(expense2)

category1 = Category('Groceries')
category2 = Category('Car Maintenance')

expense_manager.add_category(category1)
expense_manager.add_category(category2)


expense_manager.display_category()

print(budget)
expense_manager.display_total_expense()

expense_manager.remove_expense(expense2)
expense_manager.display_total_expense()
expense_manager.display_expense()
print(budget)
