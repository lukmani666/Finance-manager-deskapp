from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal
from db.models import Budget

class BudgetForm(QDialog):
    budget_added = pyqtSignal()


    def __init__(self, budget=None):
        super().__init__()

        self.setWindowTitle("Edit Budget" if budget else "Set Budget")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        self.category_input = QLineEdit(self)
        self.category_input.setPlaceholderText("Enter category")
        if budget:
            self.category_input.setText(budget.category)
        layout.addWidget(QLabel("Category: "))
        layout.addWidget(self.category_input)

        self.limit_input = QLineEdit(self)
        self.limit_input.setPlaceholderText("Enter budget limit")
        if budget:
            self.limit_input.setText(str(budget.budget_limit))
        layout.addWidget(QLabel("Limit: "))
        layout.addWidget(self.limit_input) 

        self.submit_button = QPushButton("Update Budget" if budget else "Set Budget", self)
        self.submit_button.clicked.connect(lambda: self.save_budget(budget))
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def save_budget(self, budget):
        category = self.category_input.text().strip()
        budget_limit = self.limit_input.text().strip()

        if not category:
            self.show_error("Category cannot be empty.")
            return
        elif not budget_limit:
            self.show_error("Limit cannot be empty.")
            return

        if budget:
            budget.category = category
            budget.budget_limit = budget_limit
            
            budget.save()
        else:
            new_budget = Budget(category, budget_limit)
            new_budget.save()

        self.budget_added.emit()

        self.accept()
    

    def show_error(self, message):
        error = QMessageBox()
        error.setIcon(QMessageBox.Critical)
        error.setText(message)
        error.setWindowTitle("Error")
        error.exec_()
