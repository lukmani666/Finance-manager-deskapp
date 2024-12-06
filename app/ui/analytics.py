import matplotlib.pyplot as plt
from db.database import Database

class Analytics:
    def __init__(self):
        self.db = Database()

    def get_expenses_by_category(self):
        query = "SELECT category, SUM(amount) FROM expenses GROUP BY category"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_budgets(self):
        query = "SELECT category, budget_limit FROM budgets"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()

    def plot_expenses_vs_budgets(self):
        expenses = self.get_expenses_by_category()
        budgets = self.get_budgets()

        expense_dict = {category: amount for category, amount in expenses}
        budget_dict = {category: limit for category, limit in budgets}

        categories = list(set(expense_dict.keys()).union(budget_dict.keys()))
        expense_values = [expense_dict.get(category, 0) for category in categories]
        budget_values = [budget_dict.get(category, 0) for category in categories]

        plt.bar(categories, expense_values, width=0.4, label='Expenses', align='center')
        plt.bar(categories, budget_values, width=0.4, label='Budgets', align='edge')

        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Expense vs Budget')
        plt.legend()
        plt.show()
    
    def plot_monthly_expenses(self):
        query = """
        SELECT strftime('%Y-%m', date) as month, SUM(amount) FROM expenses
        GROUP BY month
        """
        self.db.cursor.execute(query)
        results = self.db.cursor.fetchall()

        months, amounts = zip(*results)

        plt.plot(months, amounts)
        plt.xlabel('Month')
        plt.ylabel('Total Expenses')
        plt.title('Monthly Expense Breakdown')
        plt.show()
    
