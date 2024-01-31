from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from cahier_reservation import*
from pack import *
from crud import *
from infotrai import *
from home import *


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre
        self.setWindowTitle("Login Window")
        self.setGeometry(100, 100, 1000, 600)  # Larger width and height
        self.setFixedSize(1000, 550)  # La fenêtre ne peut pas être redimensionnée

        # Configuration du fond d'écran
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 1000, 600)  # Larger width and height
        self.background_label.setStyleSheet("background-color:rgb(240,249,254)")

        # LOGO
        self.logo_label = QLabel(self)
        logo_pixmap = QPixmap("logorbg.png")
        self.logo_label.setPixmap(logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignLeft)
        self.logo_label.setGeometry(20, 20, 400, 400)  # Adjust the size and position as needed
        self.logo_label.setStyleSheet("background-color: rgb(240,249,254) ;")

        # widgets
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

        # Ajouter du style CSS
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
###########################################################################

    def login(self):
        # Méthode appelée lorsque l'on clique sur le bouton de connexion
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
                print("Connexion réussie !")

                # Créez une instance de Ui_MainWindow et affichez la fenêtre principale
                self.main_window = Ui_MainWindow()
                self.main_window.setupUi(MainWindow)
                self.main_window.montrer_Home()
                self.main_window.show_main_window()

                self.close()
            else:
                print("Échec de la connexion.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:#fff;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toodle = QtWidgets.QFrame(self.frame_top)
        self.frame_toodle.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_toodle.setMaximumSize(QtCore.QSize(80, 55))
        self.frame_toodle.setStyleSheet("background:rgb(188, 229, 255);")
        self.frame_toodle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_toodle.setObjectName("frame_toodle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toodle = QtWidgets.QPushButton(self.frame_toodle)
        self.toodle.setMinimumSize(QtCore.QSize(80, 55))
        self.toodle.setMaximumSize(QtCore.QSize(80, 55))
        self.toodle.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(188, 229, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 170, 220);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.toodle.setText("")
        self.toodle.setFlat(True)
        self.toodle.setObjectName("toodle")
        self.horizontalLayout_3.addWidget(self.toodle)
        self.horizontalLayout.addWidget(self.frame_toodle)
        self.frame_top_east = QtWidgets.QFrame(self.frame_top)
        self.frame_top_east.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_top_east.setStyleSheet("background:rgb(188, 229, 255);")
        self.frame_top_east.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top_east.setObjectName("frame_top_east")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_user = QtWidgets.QFrame(self.frame_top_east)
        self.frame_user.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_user.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_user.setObjectName("frame_user")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lab_user = QtWidgets.QLabel(self.frame_user)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet("color:rgb(255,255,255);")
        self.lab_user.setText("")
        self.lab_user.setPixmap(QtGui.QPixmap("images/logorbg.png"))
        self.lab_user.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_user.setObjectName("lab_user")
        self.horizontalLayout_9.addWidget(self.lab_user)
        self.horizontalLayout_4.addWidget(self.frame_user)
        self.frame_person = QtWidgets.QFrame(self.frame_top_east)
        self.frame_person.setMinimumSize(QtCore.QSize(55, 55))
        self.frame_person.setMaximumSize(QtCore.QSize(55, 55))
        self.frame_person.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_person.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_person.setObjectName("frame_person")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_4.addWidget(self.frame_person)
        self.frame_max = QtWidgets.QFrame(self.frame_top_east)
        self.frame_max.setMinimumSize(QtCore.QSize(55, 55))
        self.frame_max.setMaximumSize(QtCore.QSize(55, 55))
        self.frame_max.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_max.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_max.setObjectName("frame_max")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bn_me = QtWidgets.QPushButton(self.frame_max)
        self.bn_me.setMaximumSize(QtCore.QSize(55, 55))
        self.bn_me.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(120, 170, 220);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_me.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/utilisateur.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_me.setIcon(icon1)
        self.bn_me.setIconSize(QtCore.QSize(24, 24))
        self.bn_me.setFlat(True)
        self.bn_me.setObjectName("bn_me")
        self.horizontalLayout_6.addWidget(self.bn_me)
        self.horizontalLayout_4.addWidget(self.frame_max)
        self.frame_close = QtWidgets.QFrame(self.frame_top_east)
        self.frame_close.setMinimumSize(QtCore.QSize(55, 55))
        self.frame_close.setMaximumSize(QtCore.QSize(55, 55))
        self.frame_close.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_close.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_close.setObjectName("frame_close")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bn_me.clicked.connect(self.montrer_InfoTraiteur)

        self.bn_close = QtWidgets.QPushButton(self.frame_close)
        self.bn_close.setMaximumSize(QtCore.QSize(55, 55))
        self.bn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(120, 170, 220);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/sortir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_close.setIcon(icon2)
        self.bn_close.setIconSize(QtCore.QSize(18, 24))
        self.bn_close.setFlat(True)
        self.bn_close.setObjectName("bn_close")
        self.bn_close.clicked.connect(self.show_login)
        self.horizontalLayout_5.addWidget(self.bn_close)
        self.horizontalLayout_4.addWidget(self.frame_close)
        self.horizontalLayout.addWidget(self.frame_top_east)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bottom.setObjectName("frame_bottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_bottom_west = QtWidgets.QFrame(self.frame_bottom)
        self.frame_bottom_west.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet("background:rgb(188, 229, 255);")
        self.frame_bottom_west.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bottom_west.setObjectName("frame_bottom_west")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_home = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_home.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_home.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_home.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_home.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_home.setObjectName("frame_home")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.bn_home = QtWidgets.QPushButton(self.frame_home)
        self.bn_home.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_home.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_home.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(120, 170, 220);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_home.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/ac.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_home.setIcon(icon3)
        self.bn_home.setIconSize(QtCore.QSize(24, 24))
        self.bn_home.setFlat(True)
        self.bn_home.setObjectName("bn_home")
        self.horizontalLayout_15.addWidget(self.bn_home)
        self.verticalLayout_3.addWidget(self.frame_home)
        self.frame_clients= QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_clients.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_clients.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_clients.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_clients.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_clients.setObjectName("frame_clients")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_clients)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.bn_home.clicked.connect(self.montrer_Home)

        self.bn_clients = QtWidgets.QPushButton(self.frame_clients)
        self.bn_clients.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_clients.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_clients.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 170, 220);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_clients.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/clients.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_clients.setIcon(icon4)
        self.bn_clients.setIconSize(QtCore.QSize(24, 24))
        self.bn_clients.setFlat(True)
        self.bn_clients.setObjectName("bn_clients")
        self.horizontalLayout_16.addWidget(self.bn_clients)
        self.verticalLayout_3.addWidget(self.frame_clients)
        self.bn_clients.clicked.connect(self.montrer_reservation_app)
        self.frame_reservation = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_reservation.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_reservation.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_reservation.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_reservation.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_reservation.setObjectName("frame_reservation")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_reservation)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.bn_reservation = QtWidgets.QPushButton(self.frame_reservation)
        self.bn_reservation.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_reservation.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_reservation.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 170, 220);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_reservation.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/calendrier-coeur.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_reservation.setIcon(icon5)
        self.bn_reservation.setIconSize(QtCore.QSize(24, 24))
        self.bn_reservation.setFlat(True)
        self.bn_reservation.setObjectName("bn_reservation")
        self.horizontalLayout_17.addWidget(self.bn_reservation)
        self.verticalLayout_3.addWidget(self.frame_reservation)
        self.frame_pack = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_pack.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_pack.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_pack.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pack.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_pack.setObjectName("frame_pack")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_pack)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.bn_reservation.clicked.connect(self.montrer_calendrier)
        self.bn_pack = QtWidgets.QPushButton(self.frame_pack)
        self.bn_pack.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_pack.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_pack.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 170, 220);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_pack.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/applications.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_pack.setIcon(icon6)
        self.bn_pack.setIconSize(QtCore.QSize(24, 24))
        self.bn_pack.setFlat(True)
        self.bn_pack.setObjectName("bn_pack")
        self.horizontalLayout_18.addWidget(self.bn_pack)
        self.verticalLayout_3.addWidget(self.frame_pack)
        self.frame_8 = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addWidget(self.frame_8)
        self.horizontalLayout_2.addWidget(self.frame_bottom_west)
        self.frame_bottom_east = QtWidgets.QFrame(self.frame_bottom)
        self.frame_bottom_east.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bottom_east.setObjectName("frame_bottom_east")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_bottom_east)
        self.frame.setStyleSheet("background:#eff9fe;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_low = QtWidgets.QFrame(self.frame_bottom_east)
        self.frame_low.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_low.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_low.setStyleSheet("")
        self.frame_low.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_low.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_low.setObjectName("frame_low")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_tab = QtWidgets.QFrame(self.frame_low)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.frame_tab.setFont(font)
        self.frame_tab.setStyleSheet("background:rgb(188, 229, 255);")
        self.frame_tab.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_tab.setObjectName("frame_tab")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_11.addWidget(self.frame_tab)
        self.verticalLayout_2.addWidget(self.frame_low)
        self.horizontalLayout_2.addWidget(self.frame_bottom_east)
        self.verticalLayout.addWidget(self.frame_bottom)
        self.bn_pack.clicked.connect(self.montrer_pack)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
###########################################################################
    def show_main_window(self):
        MainWindow.show()
###########################################################################
    def montrer_pack(self):
        # Créer une instance de la fenêtre pack_evenement
        self.PACK = pack_evenements()

        layout_frame_bottom_east = self.verticalLayout_2

    
        while layout_frame_bottom_east.count():
            item = layout_frame_bottom_east.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        layout_frame_bottom_east.addWidget(self.PACK)
        
###########################################################################

    def montrer_reservation_app(self):
        # Créer une instance de la fenêtre ReservationApp
        self.reservation_app = ReservationApp()

    # Get the vertical layout of frame_bottom_east
        layout_frame_bottom_east = self.verticalLayout_2

    # Effacer la disposition verticale
        while layout_frame_bottom_east.count():
            item = layout_frame_bottom_east.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        layout_frame_bottom_east.addWidget(self.reservation_app)
        
###########################################################################


    def montrer_calendrier(self):
        # Créer une instance de la fenêtre Cahier de reservation
        self.calendrier = cahier_reservation()

    # Obtenez la disposition verticale de frame_bottom_east
        layout_frame_bottom_east = self.verticalLayout_2

    # Effacer la disposition verticale de frame_bottom_east
        while layout_frame_bottom_east.count():
            item = layout_frame_bottom_east.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        layout_frame_bottom_east.addWidget(self.calendrier)
###########################################################################
    def montrer_Home(self):
        # Créer une instance de la fenêtre HOME
        self.home = Home()

        layout_frame_bottom_east = self.verticalLayout_2

        while layout_frame_bottom_east.count():
            item = layout_frame_bottom_east.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        layout_frame_bottom_east.addWidget(self.home)
        
###########################################################################

    def montrer_InfoTraiteur(self):
        
    # Créer une instance de la fenêtre INFOTRAITEUR
        self.info = InfoTraiteurApp()

    # Obtenez la disposition verticale de frame_bottom_east
        layout_frame_bottom_east = self.verticalLayout_2

    # Effacer la disposition verticale de frame_bottom_east
        while layout_frame_bottom_east.count():
            item = layout_frame_bottom_east.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        layout_frame_bottom_east.addWidget(self.info)
###########################################################################
    def show_login(self):
        login_window.show()
        MainWindow.close()
        
###########################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bn_me.setToolTip(_translate("MainWindow", "Me"))
        self.bn_close.setToolTip(_translate("MainWindow", "Close"))
        self.bn_home.setToolTip(_translate("MainWindow", "Home"))
        self.bn_clients.setToolTip(_translate("MainWindow", "Clients"))
        self.bn_reservation.setToolTip(_translate("MainWindow", "Reservation"))
        self.bn_pack.setToolTip(_translate("MainWindow", "Pack"))
    


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    MainWindow = QtWidgets.QMainWindow()

    sys.exit(app.exec_())
