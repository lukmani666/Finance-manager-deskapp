from db.database import Database

class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def save(self):
        db = Database()
        db.cursor.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                          (self.date, self.category, self.amount, self.description))
        db.connection.commit()
        db.close()
    
    @staticmethod
    def get_all():
        query = "SELECT date, category, amount, description FROM expenses"
        rows = Database().cursor.execute(query).fetchall()

        return [Expense(*row) for row in rows]


class Budget:
    def __init__(self, category, budget_limit):
        self.category = category
        self.budget_limit = budget_limit

    def save(self):
        db = Database()
        db.cursor.execute("INSERT INTO budgets (category, budget_limit) VALUES (?, ?)", (self.category, self.budget_limit))
        db.connection.commit()
        db.close()
    
    @staticmethod
    def get_all():
        query = "SELECT category, budget_limit FROM budgets"
        rows = Database().cursor.execute(query).fetchall()

        return [Budget(*row) for row in rows]
        

class Savings:
    def __init__(self, amount):
        self.amount = amount

    def save(self):
        db = Database()
        db.cursor.execute("INSERT INTO savings (amount) VALUES (?)", (self.amount))
        db.connection.commit()
        db.close()
    
    @staticmethod
    def get_all():
        query = "SELECT * FROM savings"
        rows = Database().cursor.execute(query).fetchall()

        return [Savings(*row) for row in rows]