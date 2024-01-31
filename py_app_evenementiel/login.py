from PyQt5.QtWidgets import (
    QApplication, QDialog, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
import mysql.connector

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre
        self.setWindowTitle("Login Window")
        self.setGeometry(100, 100, 1000, 600)
        self.setFixedSize(1000, 550)

        # Configuration du fond d'écran
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 1000, 600)
        self.background_label.setStyleSheet("background-color:rgb(240,249,254)")

        # Configuration du logo
        self.logo_label = QLabel(self)
        logo_pixmap = QPixmap("logorbg.png")
        self.logo_label.setPixmap(logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignLeft)
        self.logo_label.setGeometry(20, 20, 400, 400)
        self.logo_label.setStyleSheet("background-color: rgb(240,249,254) ;")

        # Configuration des widgets
        self.username_label = QLabel("Username:", self)
        self.password_label = QLabel("Password:", self)

        self.username_entry = QLineEdit(self)
        self.password_entry = QLineEdit(self)
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)

        # Configuration du layout
        main_layout = QHBoxLayout(self)

        # Layout pour le logo et le formulaire
        form_layout = QVBoxLayout()
        form_layout.addStretch()
        form_layout.addWidget(self.username_label)
        form_layout.addWidget(self.username_entry)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_entry)
        form_layout.addWidget(self.login_button)
        form_layout.addStretch()

        # Ajouter du style pour améliorer l'apparence du formulaire
        form_layout.setSpacing(30)
        form_layout.setContentsMargins(0, 0, 50, 50)

        main_layout.addWidget(self.logo_label)
        main_layout.addLayout(form_layout)

        self.setLayout(main_layout)

        # Ajouter du style pour améliorer l'apparence
        self.setStyleSheet(
            """
            QLabel {
                color: black;
                font-size: 20px;
            }

            QLineEdit, QPushButton {
                background-color: rgba(255, 255, 255, 0.7);
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 12px;
                font-size: 14px;
            }

            QPushButton {
                background-color: #302DBB;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 15px;
                font-size: 16px;
            }

            QPushButton:hover {
                background-color: #1A1861;
            }
            """
        )

    def login(self):
        # Method called when the login button is clicked
        username = self.username_entry.text()
        password = self.password_entry.text()

        db_config = {
            "host": 'localhost',
            "user": 'root',
            "password": '',
            "database": 'traiteur',
        }

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Remplacez-le par votre requête MySQL
            query = "SELECT * FROM utilisateur WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))

            user = cursor.fetchone()

            if user:
                print("Login successful!")
                
                self.accept()
            else:
                print("Login failed.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
