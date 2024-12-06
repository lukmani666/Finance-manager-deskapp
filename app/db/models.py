from db.database import Database

class Expense:
    def __init__(self, id, date, category, amount, description):
        self.id = id
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def save(self):
        db = Database()
        if self.id:
            db.cursor.execute("""
                UPDATE expenses
                SET date = ?, category = ?, amount = ?, description = ?
                WHERE id = ?
            """, (self.date, self.category, self.amount, self.description, self.id))
        else:
            db.cursor.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                            (self.date, self.category, self.amount, self.description))
        db.connection.commit()
        db.close()
    
    @staticmethod
    def get_all():
        query = "SELECT id, date, category, amount, description FROM expenses"
        rows = Database().cursor.execute(query).fetchall()

        return [Expense(*row) for row in rows]
    
    def delete(self):
        db = Database()
        db.connection.cursor().execute("DELETE FROM expenses WHERE id = ?", (self.id,))
        db.connection.commit()


class Budget:
    def __init__(self, id, category, budget_limit):
        self.id = id
        self.category = category
        self.budget_limit = budget_limit

    def save(self):
        db = Database()
        if self.id:
            db.cursor.execute("""
                UPDATE budgets
                SET category = ?, budget_limit = ?
                WHERE id = ?
            """, (self.category, self.budget_limit, self.id))
        else:
            db.cursor.execute("INSERT INTO budgets (category, budget_limit) VALUES (?, ?)", (self.category, self.budget_limit))
        db.connection.commit()
        db.close()
    
    @staticmethod
    def get_all():
        query = "SELECT id, category, budget_limit FROM budgets"
        rows = Database().cursor.execute(query).fetchall()

        return [Budget(*row) for row in rows]
    
    def delete(self):
        db = Database()
        db.connection.cursor().execute("DELETE FROM budgets WHERE id = ?", (self.id,))
        db.connection.commit()
        
        

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