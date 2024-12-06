from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from db.models import Savings

class SavingsForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add savings")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Enter savings amount")
        layout.addWidget(QLabel("Amount: "))
        layout.addWidget(self.amount_input)

        self.submit_button = QPushButton("Add Savings", self)
        self.submit_button.clicked.connect(self.add_savings)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
    
    def add_savings(self):
        amount_text = self.amount_input.text().strip()

        try:
            amount = float(amount_text)
            if amount <= 0:
                self.show_error("Amount must be a positive number.")
                return
        except ValueError:
            self.show_error("Amount must be a valid number.")
            return
        
        savings = Savings(amount)
        savings.save()
        self.close()