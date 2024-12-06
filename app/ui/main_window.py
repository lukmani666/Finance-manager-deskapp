from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from ui.expense_form import ExpenseForm
from ui.budget_form import BudgetForm
from ui.analytics import Analytics
from ui.budget_list import BudgetList
from ui.expense_list import ExpenseList

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Finance Manager")
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel("Welcome to the Personal Finance Manager!", self)
        self.label.setStyleSheet("font-size: 18px; padding: 20px;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)

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
        self.expense_form.exec_()
    
    def open_budget_form(self):
        self.budget_form = BudgetForm()
        self.budget_form.exec_()
    
    def open_expense_form_update(self):
        self.expense_form_update = ExpenseList()
        self.expense_form_update.exec_()
    
    def open_budget_form_update(self):
        self.budget_form_update = BudgetList()
        self.budget_form_update.exec_()
    
    def view_analytics(self):
        analytics = Analytics()
        analytics.plot_expenses_vs_budgets()
    
    def monthly_analytics(self):
        analytics = Analytics()
        analytics.plot_monthly_expenses()