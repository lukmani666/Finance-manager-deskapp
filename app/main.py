import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from db.database import Database


def main():

    db = Database()
    db.create_tables()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()