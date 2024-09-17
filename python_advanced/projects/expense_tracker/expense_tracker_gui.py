from tkinter import ttk
from tkinter import simpledialog
import customtkinter as ctk
from tkcalendar import DateEntry
from expense_tracker import Expense, Category, ExpenseManager
from datetime import datetime

class SetupDialog(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.geometry("300x300")
        self.title("Setup")

        self.expense_currency = ctk.CTkLabel(self, text="Choose Currency")
        self.expense_currency.pack(pady=10)

        self.currency_var = ctk.StringVar(value="Select Currency")
        self.currency_menu = ctk.CTkOptionMenu(self, variable=self.currency_var, values=["₦", "$", "£", "€"])
        self.currency_menu.pack(pady=10)

        self.income_label = ctk.CTkLabel(self, text="Set Income")
        self.income_label.pack(pady=10)

        self.income_entry = ctk.CTkEntry(self)
        self.income_entry.pack(pady=10)

        self.submit_button = ctk.CTkButton(self, text="Done", command=self.submit_setup)
        self.submit_button.pack(pady=20)

    def submit_setup(self):
        selected_currency = self.currency_var.get()
        income = self.income_entry.get()

        if not income:
            income = 0.0
        else:
            income = income

        self.master.currency_symbol = selected_currency
        self.master.income = income

        if hasattr(self.master, 'update_income_label'):
            self.master.update_income_label()  # Update the budget label in the main window
        
        self.destroy()

class ExpenseTrackerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # appearance
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Main application window
        self.title("Expense Tracker")
        self.geometry("1200x650")

        # grid configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.currency_symbol = ""
        self.income = 0.0

        # Initialize the app
        self.setup_dialog = SetupDialog(self)
        self.wait_window(self.setup_dialog)
        self.income = float(self.income)
        self.total_expense = 0.0
        self.expense_manager = ExpenseManager(income=self.income)

        self.initial_income = f"{self.currency_symbol}{self.income}"

        # Initialize UI components
        self.initialize_widgets()

    def initialize_widgets(self):
        self.initialize_expense_tab()
        self.initialize_category_management()
        self.initialize_expense_table()
        self.update_budget_label()

    def initialize_expense_tab(self):
        cool_font = ("Roboto", 14)
        heading_font = ("Roboto", 16, "bold")
        self.top_left_frame = ctk.CTkFrame(self, border_width=2, width=350)
        self.top_left_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsw')

        # Heading
        self.expense_tab = ctk.CTkLabel(self.top_left_frame, text="Manage Expenses", font=heading_font)
        self.expense_tab.grid(row=0, column=0, pady=(10, 0))

        # Vertical line below the heading
        self.line_frame = ctk.CTkFrame(self.top_left_frame, height=1, width=220, fg_color="grey")
        self.line_frame.grid(padx=10, pady=(1, 5), row=1, column=0)

        # Center the content
        self.top_left_frame.grid_rowconfigure(10, weight=1)
        self.top_left_frame.grid_columnconfigure(0, weight=1)

        # Widgets for expense tab
        self.exp_tab_description_label = ctk.CTkLabel(self.top_left_frame, text="Description", font=cool_font)
        self.exp_tab_description_label.grid(row=2, pady=(5, 0))
        self.exp_tab_description_entry = ctk.CTkEntry(self.top_left_frame, font=cool_font, width=200)
        self.exp_tab_description_entry.grid(row=3, pady=(0, 0))
        self.exp_tab_category_label = ctk.CTkLabel(self.top_left_frame, text="Choose Category", font=cool_font)
        self.exp_tab_category_label.grid(pady=(5, 2))
        self.exp_tab_category_menu = ctk.CTkOptionMenu(self.top_left_frame, values=['Food', 'Rent & Utilities', 'Transportation', 'Entertainment', ], font=cool_font, width=200)
        self.exp_tab_category_menu.set("Select Category")
        self.exp_tab_category_menu.grid(row=5, column=0, pady=(3, 0))
        self.exp_tab_amount_label = ctk.CTkLabel(self.top_left_frame, text="Amount", font=cool_font)
        self.exp_tab_amount_label.grid(row=6, column=0, pady=(0, 2))
        self.exp_tab_amount_entry = ctk.CTkEntry(self.top_left_frame, font=cool_font, width=200)
        self.exp_tab_amount_entry.grid(row=7, column=0, pady=(0, 5))
        self.exp_tab_date_label = ctk.CTkLabel(self.top_left_frame, text="Date", font=cool_font)
        self.exp_tab_date_label.grid(row=8, column=0, pady=(0, 2))
        self.exp_tab_date_entry = DateEntry(self.top_left_frame, font=cool_font, width=15)
        self.exp_tab_date_entry.grid(row=9, column=0, pady=(0, 5))
        self.add_exp_button = ctk.CTkButton(self.top_left_frame, text="Add Expense", font=cool_font, command=self.add_expense)
        self.add_exp_button.grid(row=10, column=0, pady=(5, 5))

    def initialize_category_management(self):
        cool_font = ("Roboto", 14)
        heading_font = ("Roboto", 16, "bold")

        # Manage Category frame
        self.bottom_left_frame = ctk.CTkFrame(self, border_width=2, width=350)
        self.bottom_left_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky='nsw')
        self.bottom_left_frame.grid_rowconfigure(7, weight=1)
        self.bottom_left_frame.grid_columnconfigure(0, weight=1)

        # Manage Category Heading
        self.cat_name_label = ctk.CTkLabel(self.bottom_left_frame, text="Manage Categories", font=heading_font)
        self.cat_name_label.grid(row=0, column=0, pady=(2))
        self.cat_line_frame = ctk.CTkFrame(self.bottom_left_frame, height=1, width=220, fg_color="grey")
        self.cat_line_frame.grid(row=1, column=0, padx=10, pady=(1, 5))
        self.cat_add_label = ctk.CTkLabel(self.bottom_left_frame, text="Category name", font=cool_font)
        self.cat_add_label.grid(row=2, column=0, pady=(5, 0))
        self.cat_name_entry = ctk.CTkEntry(self.bottom_left_frame, font=cool_font, width=200)
        self.cat_name_entry.grid(row=3, column=0, pady=(0, 0))
        self.add_cat_button = ctk.CTkButton(self.bottom_left_frame, text="Add Category", font=cool_font, command=self.add_category)
        self.add_cat_button.grid(row=4, column=0, pady=(10, 5))
        self.cat_delete_label = ctk.CTkLabel(self.bottom_left_frame, text="Delete Category", font=cool_font)
        self.cat_delete_label.grid(row=5, column=0, pady=(20, 0))
        self.cat_tab_delete_menu = ctk.CTkOptionMenu(self.bottom_left_frame, values=['Food', 'Rent & Utilities', 'Transportation', 'Entertainment', 'Health'], font=cool_font, width=200)
        self.cat_tab_delete_menu.set("Select Category")
        self.cat_tab_delete_menu.grid(row=6, column=0, pady=(0, 1))
        self.remove_cat_button = ctk.CTkButton(self.bottom_left_frame, text="Remove Category", font=cool_font, command=self.delete_category)
        self.remove_cat_button.grid(row=7, column=0, pady=(0, 20))

    def initialize_expense_table(self):
        cool_font = ("Roboto", 14)
        heading_font = ("Roboto", 16, "bold")
        amount_font = ("Roboto", 20, "bold")

        # Expense table frame
        self.expense_table_frame = ctk.CTkFrame(self, border_width=2, height=500)
        self.expense_table_frame.grid(row=0, column=1, padx=(0, 5), pady=(10), rowspan=2, sticky="nsew")
        self.expense_table_frame.grid_rowconfigure(0, weight=0)
        self.expense_table_frame.grid_rowconfigure(1, weight=1)
        self.expense_table_frame.grid_columnconfigure(1, weight=1)

        # expense table heading 
        self.heading_label = ctk.CTkLabel(self.expense_table_frame, text="Expenses", font=("Arial", 16, "bold"))
        self.heading_label.grid(row=0, padx=5, pady=(2, 0), sticky="nsew")

        # Save expense Button
        self.save_expense_button = ctk.CTkButton(self.expense_table_frame, text='Clear',width=60 , font=cool_font, command=self.clear_expenses)
        self.save_expense_button.grid(row=0, padx=10, pady=(10, 5)  , sticky='e')

        # summary frame
        self.summary_frame = ctk.CTkFrame(self.expense_table_frame, border_width=2)
        self.summary_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.summary_frame.grid_columnconfigure(0, weight=1)
        self.summary_frame.grid_columnconfigure(1, weight=1)
        self.summary_frame.grid_columnconfigure(2, weight=1)
        self.summary_frame.grid_rowconfigure(0, weight=1)

        # Left Frame
        self.left_summary_frame = ctk.CTkFrame(self.summary_frame, border_width=2, fg_color='white')
        self.left_summary_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.left_summary_frame.grid_rowconfigure(0, weight=1)
        self.left_summary_frame.grid_columnconfigure(0, weight=1)

        self.income_heading = ctk.CTkLabel(self.left_summary_frame, text="Income", font=heading_font)
        self.income_heading.grid(padx=10, pady=(5, 5), sticky='nsew')

        self.income_label = ctk.CTkLabel(self.left_summary_frame, text=f"{self.initial_income}", font=amount_font)
        self.income_label.grid(row=1, padx=10, pady=(0 ,10), sticky='nsew')

        # Middle Frmae - Total Expense
        self.middle_summary_frame = ctk.CTkFrame(self.summary_frame, border_width=2, fg_color='white')
        self.middle_summary_frame.grid(row=0, column=1, pady=10, sticky="nsew")
        self.middle_summary_frame.grid_rowconfigure(0, weight=1)
        self.middle_summary_frame.grid_columnconfigure(0, weight=1)

        self.middle_heading = ctk.CTkLabel(self.middle_summary_frame, text="Total Expense", font=heading_font)
        self.middle_heading.grid(row=0, column=0, padx=10, pady=(5, 5), sticky='nsew')

        self.total_expense_label = ctk.CTkLabel(self.middle_summary_frame, text=f"{self.currency_symbol} {self.total_expense}", font=amount_font)
        self.total_expense_label.grid(row=2, padx=10, pady=(0, 10), sticky='nsew')

        # Right Frame - Amount Left
        self.right_summary_frame = ctk.CTkFrame(self.summary_frame, border_width=2, fg_color='white')
        self.right_summary_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.right_summary_frame.grid_rowconfigure(0, weight=1)
        self.right_summary_frame.grid_columnconfigure(0, weight=1)

        self.right_heading = ctk.CTkLabel(self.right_summary_frame, text="Amount left", font=heading_font)
        self.right_heading.grid(row=0, column=0, padx=10, pady=(5, 5), sticky='nsew')

        self.amount_left_label = ctk.CTkLabel(self.right_summary_frame, text=f"{self.currency_symbol} {self.income}", font=amount_font)
        self.amount_left_label.grid(padx=10, pady=(0, 10), sticky='nsew')
        
        self.create_expense_table()

    def create_expense_table(self):
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14))
        style.configure("Treeview.Heading", font=("Arial", 16, "bold"))

        columns = ("#1", "#2", "#3", "#4")
        self.expense_table = ttk.Treeview(self.expense_table_frame, columns=columns, show='headings')

        # Define headings
        self.expense_table.heading("#1", text="Description")
        self.expense_table.heading("#2", text="Category")
        self.expense_table.heading("#3", text="Date")
        self.expense_table.heading("#4", text="Amount")

        # Define column widths
        self.expense_table.column("#1", anchor='center', width=200)
        self.expense_table.column("#2", anchor='center', width=150)
        self.expense_table.column("#3", anchor='center', width=100)
        self.expense_table.column("#4", anchor='center', width=100)

        self.expense_table.grid(row=1, padx=10, pady=(0, 5), rowspan=1, sticky='nsew')

        # Add a scrollbar if needed
        self.scrollbar = ttk.Scrollbar(self.expense_table_frame, orient="vertical", command=self.expense_table.yview)
        self.expense_table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=1, sticky='ns', padx=(0, 10), pady=10)

        # Ensure the frame expands
        self.expense_table_frame.grid_columnconfigure(0, weight=1)
        self.expense_table_frame.grid_columnconfigure(1, weight=0)

    def add_expense(self):
        description = self.exp_tab_description_entry.get().title()
        category = self.exp_tab_category_menu.get().title()
        date = self.exp_tab_date_entry.get_date()
        amount = float(self.exp_tab_amount_entry.get())
        formatted_amount = f"{self.currency_symbol}{amount:,.2f}"

        self.income -= amount

        expense = Expense(expense_amount=amount, expense_description=description, date=date)
        self.expense_manager.add_expense(expense)

        self.expense_table.insert("", "end", values=(description, category, date, formatted_amount))

        self.exp_tab_description_entry.delete(0, 'end')
        self.exp_tab_category_menu.set("Select Category")
        self.exp_tab_date_entry.set_date(datetime.today())
        self.exp_tab_amount_entry.delete(0, 'end')

        self.update_total_expense_label()
        self.update_budget_label()

    def add_category(self):
        category_name = self.cat_name_entry.get()
        if category_name:
            new_category = Category(category_name)
            try:
                self.expense_manager.add_category(new_category)
                categories = [cat.category_name for cat in self.expense_manager.categories]

                self.exp_tab_category_menu.configure(values=categories)
                self.cat_tab_delete_menu.configure(values=categories)
                self.exp_tab_category_menu.set(category_name)
                self.cat_name_entry.delete(0, 'end')
            except Exception as e:
                print(e)

    def delete_category(self):
        selected_category = self.cat_tab_delete_menu.get()
        if selected_category != "Select Category":
            category_to_remove = next((cat for cat in self.expense_manager.categories if cat.category_name == selected_category), None)
            if category_to_remove:
                try:
                    self.expense_manager.remove_category(category_to_remove)
                    # Update the category option menu
                    categories = [cat.category_name for cat in self.expense_manager.categories]
                    self.exp_tab_category_menu.configure(values=categories)
                    self.cat_tab_delete_menu.configure(values=categories)

                    self.cat_tab_delete_menu.set("Select Category")
                    self.exp_tab_category_menu.set("Select Category")
                except Exception as e:
                    print(e)

    def update_total_expense_label(self):
        total_expense = self.expense_manager.total_expense
        self.total_expense_label.configure(text=f"{self.currency_symbol} {total_expense:,.2f}")

    def update_budget_label(self):
        self.amount_left_label.configure(text=f"{self.currency_symbol} {self.income:,.2f}")

    def update_amount_left_label(self):
        amount_left = self.expense_manager.amount_left
        self.amount_left_label.configure(text=f"{self.currency_symbol} {amount_left:,.2f}")


    def clear_expenses(self):
        for item in self.expense_table.get_children():
            self.expense_table.delete(item)
            
        self.expenses = []
        self.expense_manager.total_expense = 0.0

        self.update_total_expense_label()
        self.update_amount_left_label()


app = ExpenseTrackerGUI()
app.mainloop()

