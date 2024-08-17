import customtkinter as ctk

class ExpenseTrackerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Main application window
        self.title("Expense Tracker")
        self.geometry("1200x650")

        # grid configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # left tab
        self.top_left_frame = ctk.CTkFrame(self)
        self.top_left_frame.grid(padx=10, pady=10, row=0, column=0, rowspan=2, sticky='nsew')

        # Label (Manage Expenses)
        # Heading
        self.expense_tab = ctk.CTkLabel(self.top_left_frame, text="Manage Expences")
        self.expense_tab.grid()

        # Label - Description
        self.exp_tab_description_label = ctk.CTkLabel(self.top_left_frame, text="Decription")
        self.exp_tab_description_label.grid()
        
        # Entry ()
        self.exp_tab_description_entry = ctk.CTkEntry(self.top_left_frame)
        self.exp_tab_description_entry.grid()

        # Label - Category
        self.exp_tab_category_label = ctk.CTkLabel(self.top_left_frame, text="Choose Category")
        self.exp_tab_category_label.grid()

        # Option menu
        self.exp_tab_category_label = ctk.CTkOptionMenu(self.top_left_frame)
        self.exp_tab_category_label.grid()

        # # Entry ()
        # self.exp_tab_amount_entry = ctk.CTkEntry(self.left_frame)
        # self.exp_tab_amount_entry.grid()

        # Label - Amount
        self.exp_tab_amount_label = ctk.CTkLabel(self.top_left_frame, text="Amount")
        self.exp_tab_amount_label.grid()

        # Entry ()
        self.exp_tab_amount_entry = ctk.CTkEntry(self.top_left_frame)
        self.exp_tab_amount_entry.grid()

        # Button
        self.add_exp_button = ctk.CTkButton(self.top_left_frame, text="Add Expense")
        self.add_exp_button.grid()

        # Label (Manage Expenses)

        self.bottom_left_frame = ctk.CTkFrame(self)
        self.bottom_left_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        # Label - Cat name 
        self.cat_name_label = ctk.CTkLabel(self.bottom_left_frame, text="Category")
        self.cat_name_label.grid()

        self.cat_name_entry = ctk.CTkEntry(self.bottom_left_frame)
        self.cat_name_entry.grid()

        self.add_cat_button = ctk.CTkButton(self.bottom_left_frame, text="Add Category")
        self.add_cat_button.grid()

        # Expense table frame
        self.expense_table_frame = ctk.CTkFrame(self)
        self.expense_table_frame.grid(padx=(10), pady=(10), row=0, column=1, rowspan=2, columnspan=3, sticky='nsew')

        # Chart frame
        self.chart_frame = ctk.CTkFrame(self)
        self.chart_frame.grid(padx=10, pady=(0, 10), row=2, column=1, columnspan=2, sticky='nsew')

        # total frame
        self.total_frame = ctk.CTkFrame(self)
        self.total_frame.grid(padx=10, pady=(0, 10), row=2, column=3, sticky='nsew')

        # self.total_frame.grid_rowconfigure(0, weight=1)
        # self.total_frame.grid_rowconfigure(1, weight=1)
        # self.total_frame.grid_columnconfigure(0, weight=1)


        # self.top_total_frame = ctk.CTkFrame(self.total_frame)
        # self.top_total_frame.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="nsew")

        # self.bottom_total_frame = ctk.CTkFrame(self.total_frame)
        # self.bottom_total_frame.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="nsew")


        
app = ExpenseTrackerGUI()
app.mainloop()
