from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import pyqtSignal
from db.models import Expense
from ui.expense_form import ExpenseForm

class ExpenseList(QDialog):
    expense_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Expenses")
        self.setGeometry(300, 300, 400, 400)

        layout = QVBoxLayout()

        expenses = Expense.get_all()

        for expense in expenses:
            hbox = QHBoxLayout()

            expense_label = QLabel(f"{expense.category}: {expense.amount}")
            hbox.addWidget(expense_label)

            edit_button = QPushButton("Edit", self)
            edit_button.clicked.connect(lambda _, e=expense: self.edit_expense(e))
            hbox.addWidget(edit_button)

            delete_button = QPushButton("Delete", self)
            delete_button.clicked.connect(lambda _, e=expense: self.delete_expense(e))
            hbox.addWidget(delete_button)

            layout.addLayout(hbox)
        
        self.setLayout(layout)
    
    def edit_expense(self, expense):
        self.edit_form = ExpenseForm(expense=expense)
        self.edit_form.exec_()
        self.expense_signal.emit()
        self.accept()
    
    def delete_expense(self, expense):
        expense.delete()
        self.expense_signal.emit()
        self.accept()