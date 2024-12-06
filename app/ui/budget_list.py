from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from db.models import Budget
from ui.budget_form import BudgetForm

class BudgetList(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Budgets")
        self.setGeometry(300, 300, 400, 400)

        layout = QVBoxLayout()

        budgets = Budget.get_all()

        for budget in budgets:
            hbox = QHBoxLayout()

            expense_label = QLabel(f"{budget.category}: {budget.budget_limit}")
            hbox.addWidget(expense_label)

            edit_button = QPushButton("Edit", self)
            edit_button.clicked.connect(lambda _, b=budget: self.edit_expense(b))
            hbox.addWidget(edit_button)

            delete_button = QPushButton("Delete", self)
            delete_button.clicked.connect(lambda _, b=budget: self.delete_expense(b))
            hbox.addWidget(delete_button)

            layout.addLayout(hbox)
        
        self.setLayout(layout)
    
    def edit_expense(self, budget):
        self.edit_form = BudgetForm(budget=budget)
        self.edit_form.exec_()
    
    def delete_expense(self, budget):
        budget.delete()
        self.close()