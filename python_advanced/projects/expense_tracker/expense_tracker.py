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
    
class Income:
    def __init__(self, income: float):
        self.income = income

    def add_income(self, amount: float):
        if amount > 0:
            self.income += amount
        else:
            return f"Amount must be positive"
        
    def deduct_income(self, amount: float):
        if amount > 0:
            if amount <= self.self.income:
                self.income -= amount
            else:
                print("Insufficient funds")
        else:
            print("Amount must be positive")

    def __str__(self):
        return f"Income: ₦{self.income:.2f}"

class ExpenseManager:
    def __init__(self, income):
        self.income = income
        self.total_expense = 0
        self.expenses = []
        self.categories = []

    def add_expense(self, expense: Expense):
        if expense not in self.expenses:
            self.expenses.append(expense)
            self.total_expense += expense.expense_amount
            self.income.deduct_income(expense.expense_amount)
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
            self.income.add_income(expense.expense_amount)
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
 
