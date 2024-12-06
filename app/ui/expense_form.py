from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from db.models import Expense

class ExpenseForm(QDialog):
    def __init__(self, expense=None):
        super().__init__()

        self.setWindowTitle("Edit Expense" if expense else "Add Expense")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        self.date_input = QLineEdit(self)
        self.date_input.setPlaceholderText("Enter date (YYYY-MM-DD)")
        if expense:
            self.date_input.setText(expense.date)
        layout.addWidget(QLabel("Date: "))
        layout.addWidget(self.date_input)

        self.category_input = QLineEdit(self)
        self.category_input.setPlaceholderText("Enter category")
        if expense:
            self.category_input.setText(expense.category)
        layout.addWidget(QLabel("Category: "))
        layout.addWidget(self.category_input)

        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Enter amount")
        if expense:
            self.amount_input.setText(str(expense.amount))
        layout.addWidget(QLabel("Amount: "))
        layout.addWidget(self.amount_input)

        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Enter description")
        if expense:
            self.description_input.setText(str(expense.description))
        layout.addWidget(QLabel("Description: "))
        layout.addWidget(self.description_input)

        self.submit_button = QPushButton("Update Expense" if expense else "Add Expense", self)
        self.submit_button.clicked.connect(lambda: self.save_expense(expense))
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
    

    def save_expense(self, expense):
        date = self.date_input.text()
        category = self.category_input.text().strip()
        amount_text = self.amount_input.text().strip()
        description = self.description_input.text()

        if not category:
            self.show_error("Category cannot be empty.")
            return

        try:
            amount = float(amount_text)
            if amount <= 0:
                self.show_error("Amount must be a positive number.")
                return
        except ValueError:
            self.show_error("Amount must be a valid number.")
            return
        
        if expense:
            expense.date
            expense.category = category
            expense.amount = amount
            expense.description = description
            expense.save()
        else:
            new_expense = Expense(date, category, amount, description)
            new_expense.save()

        self.close()
    
    def show_error(self, message):
        error = QMessageBox()
        error.setIcon(QMessageBox.Critical)
        error.setText(message)
        error.setWindowTitle("Error")
        error.exec_()