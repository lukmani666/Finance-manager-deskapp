from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from ui.expense_form import ExpenseForm
from ui.budget_form import BudgetForm
from ui.analytics import Analytics
from ui.budget_list import BudgetList
from ui.expense_list import ExpenseList
from db.models import Expense
from db.models import Budget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Finance Manager")
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel("Welcome to the Personal Finance Manager!", self)
        self.label.setStyleSheet("font-size: 18px; padding: 20px;")
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.expense_table_title = QLabel("Expense List", self)
        self.expense_table_title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(self.expense_table_title)

        self.expense_table = QTableWidget(self)
        self.expense_table.setColumnCount(4)
        self.expense_table.setHorizontalHeaderLabels(["Date", "Category", "Amount", "Description"])
        layout.addWidget(self.expense_table)

        self.load_expenses()

        self.budget_table_title = QLabel("Budget List", self)
        self.budget_table_title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(self.budget_table_title)

        self.budget_table = QTableWidget(self)
        self.budget_table.setColumnCount(2)
        self.budget_table.setHorizontalHeaderLabels(["Category", "budget_limit"])
        layout.addWidget(self.budget_table)

        self.load_budgets()

        self.add_expense_button = QPushButton("Add Expense", self)
        self.add_expense_button.clicked.connect(self.open_expense_form)
        layout.addWidget(self.add_expense_button)

        self.set_budget_button = QPushButton("Set Budget", self)
        self.set_budget_button.clicked.connect(self.open_budget_form)
        layout.addWidget(self.set_budget_button)

        self.update_expense_button = QPushButton("Edit Expanse", self)
        self.update_expense_button.clicked.connect(self.open_expense_form_update)
        layout.addWidget(self.update_expense_button)

        self.update_budget_button = QPushButton("Edit Budget", self)
        self.update_budget_button.clicked.connect(self.open_budget_form_update)
        layout.addWidget(self.update_budget_button)

        self.view_analytics_button = QPushButton("View Analytics", self)
        self.view_analytics_button.clicked.connect(self.view_analytics)
        layout.addWidget(self.view_analytics_button)

        self.monthly_analytics_button = QPushButton("Monthly Analytics", self)
        self.monthly_analytics_button.clicked.connect(self.monthly_analytics)
        layout.addWidget(self.monthly_analytics_button)


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def open_expense_form(self):
        self.expense_form = ExpenseForm()
        self.expense_form.expense_added.connect(self.load_expenses)
        self.expense_form.exec_()
    
    def open_budget_form(self):
        self.budget_form = BudgetForm()
        self.budget_form.budget_added.connect(self.load_budgets)
        self.budget_form.exec_()
    
    def open_expense_form_update(self):
        self.expense_form_update = ExpenseList()
        self.expense_form_update.expense_signal.connect(self.load_expenses)
        self.expense_form_update.exec_()
    
    def open_budget_form_update(self):
        self.budget_form_update = BudgetList()
        self.budget_form_update.budget_signal.connect(self.load_budgets)
        self.budget_form_update.exec_()
    
    def view_analytics(self):
        analytics = Analytics()
        analytics.plot_expenses_vs_budgets()
    
    def monthly_analytics(self):
        analytics = Analytics()
        analytics.plot_monthly_expenses()
    
    def load_expenses(self):
        """Load all expenses from the database and display them in the table."""
        expenses = Expense.get_all()
        self.expense_table.setRowCount(0)

        for expense in expenses:
            row_position = self.expense_table.rowCount()
            self.expense_table.insertRow(row_position)

            self.expense_table.setItem(row_position, 0, QTableWidgetItem(expense.date))
            self.expense_table.setItem(row_position, 1, QTableWidgetItem(expense.category))
            self.expense_table.setItem(row_position, 2, QTableWidgetItem(str(expense.amount)))
            self.expense_table.setItem(row_position, 3, QTableWidgetItem(expense.description))
    
    def load_budgets(self):
        """Load all budgets from the database and display them in the table."""
        budgets = Budget.get_all()
        self.budget_table.setRowCount(0)

        for budget in budgets:
            row_position = self.budget_table.rowCount()
            self.budget_table.insertRow(row_position)

            self.budget_table.setItem(row_position, 0, QTableWidgetItem(budget.category))
            self.budget_table.setItem(row_position, 1, QTableWidgetItem(str(budget.budget_limit)))
