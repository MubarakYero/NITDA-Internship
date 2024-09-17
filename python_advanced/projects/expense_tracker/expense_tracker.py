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
            
class Category:
    def __init__(self, category_name):
        self.category_name = category_name

    def __str__(self):
        return f"Category Name: {self.category_name}"

class ExpenseManager:
    def __init__(self, income):
        self.income = income
        self.total_expense = 0.0
        self.amount_left = self.income - self.total_expense
        self.expenses = []
        self.categories = []

    def add_expense(self, expense: Expense):
        if expense not in self.expenses:
            self.expenses.append(expense)
            self.total_expense += expense.expense_amount
            self.income -= expense.expense_amount
        else:
            print(f"Expense '{expense}' already exists")

    def remove_expense(self, expense: Expense):
        try:    
            self.expenses.remove(expense)
            self.total_expense -= expense.expense_amount
            self.income += expense.expense_amount
        except ValueError:
            raise(f"Expense '{expense}' not found")
        
    def add_category(self, category):
        if category not in self.categories: 
            self.categories.append(category)
        else:
            raise(f"Category '{category.category_name}' already exists.")

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

    def display_income(self):
        print(f"Remaining Income: ₦{self.income}")

    def display_total_expense(self):
        print(f"Total Expense: ₦{self.total_expense:.2f}")

# exp_manager = ExpenseManager(12000)

# exp1 = Expense(1000, 'Party', date(2023, 8, 20))
# exp2 = Expense(1500, 'Groceries', date(2023, 8, 21))

# exp_manager.add_expense(exp1)
# exp_manager.add_expense(exp2)

# # exp_manager.display_expense()
# exp_manager.display_total_expense()
# exp_manager.display_income()

# exp_manager.remove_expense(exp1)
# exp_manager.display_total_expense()
