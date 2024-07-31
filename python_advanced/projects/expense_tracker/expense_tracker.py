# Expense tracker

# Expense class to handle individual expenses
class Expense:
    def __init__(self, id=None, amount=0, description='', date='', category=''):
        self.id = id
        self.amount = amount
        self.description = description
        self.date = date
        self.category = category

        print(self.id, self.amount, self.description, self.date, self.category)
    
    def edit_expense(self, id=None, amount=None, description=None, date=None, category=None):
        if id != None:
            self.id = id
        if amount != None:
            self.amount = amount
        if description != None:
            self.description = description
        if date != None:
            self.date = date
        if category != None:
            self.category = category

    def display(self):
        print(f"ID: {self.id}, Amount: {self.amount}, Description: {self.description}, Date: {self.date}, Category: {self.category}")

# Category class to handle different expense categories

class Categories:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Category: {self.name}")



    
