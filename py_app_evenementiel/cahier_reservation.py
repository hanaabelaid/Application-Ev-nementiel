from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QCalendarWidget, QTextEdit, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate
from PyQt5 import QtGui
import mysql.connector

class cahier_reservation(QWidget):
    def __init__(self):
        super().__init__()

        self.reservations = {}  # Dictionnaire pour stocker les reservations

        self.initUI()

    def initUI(self):
        
        # Layout principal
        layout = QVBoxLayout()

        # Calendrier
        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.show_reservation)
        layout.addWidget(self.calendar)

        # Zone de texte pour afficher le nom du client
        self.client_name_display = QTextEdit(self)
        self.client_name_display.setReadOnly(True)
        self.client_name_display.setFixedHeight(50)  
        layout.addWidget(self.client_name_display)


        
        # Appliquer le layout principal à la fenêtre
        self.setLayout(layout)


        # Ajouter les réservations initiales
        self.init_reservations_from_db()
        self.update_calendar()

###########################################################################

    def init_reservations_from_db(self):
        try:
            # Ouvrir une connexion à la base de données
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='traiteur'
            )
            cursordb = con.cursor()

            # Sélectionner les réservations depuis la table reservations
            query_select_reservations = "SELECT nom, prenom,date FROM client"
            cursordb.execute(query_select_reservations)
            result = cursordb.fetchall()

            # Stocker les réservations dans le dictionnaire reservations
            for nom, prenom, date in result:
                # Convertir le datetime.date en QDate
                year, month, day = date.year, date.month, date.day
                reservation_date = QDate(year, month, day)
                self.reservations[reservation_date] = f"{nom} {prenom}"
            # Fermer la connexion à la base de données
            con.close()

            # Appliquer les fonctions de la classe aux dates sélectionnées
            self.show_reservation()
            self.update_calendar()

        except Exception as e:
            # Gestion des exceptions avec un message d'erreur
            print("Erreur :", e)

###########################################################################

    def show_confirmation(self):
        # Obtenir la date sélectionnée et le nom du client
        selected_date = self.calendar.selectedDate()
        client_name = self.client_name_display.toPlainText().strip()

        # Si aucun nom de client n'est saisi, utiliser "Client Anonyme"
        if not client_name:
            client_name = "Client Anonyme"

        # Vérifier si la date est déjà réservée
        if selected_date not in self.reservations:
            # Enregistrer la réservation et mettre à jour le calendrier
            self.reservations[selected_date] = client_name
            self.update_calendar()
            self.client_name_display.clear()

###########################################################################
    def show_reservation(self):
        # Afficher le nom du client réservant la date sélectionnée
        selected_date = self.calendar.selectedDate()
        if selected_date in self.reservations:
            client_name = self.reservations[selected_date]
            self.client_name_display.setPlainText(f"Réservé par : {client_name}")
        else:
            # Effacer le texte si la date n'est pas réservée
            self.client_name_display.clear()

###########################################################################
# Mettre à jour le calendrier avec les réservations
    def update_calendar(self):
        for date, client_name in self.reservations.items():
            self.calendar.setDateTextFormat(date, self.create_format(client_name))

###########################################################################
# Créer un format de texte avec une couleur de texte bleue et un fond gris clair
    def create_format(self, client_name):
        format = QtGui.QTextCharFormat()
        format.setForeground(QtGui.QBrush(Qt.blue))
        format.setBackground(QtGui.QBrush(Qt.lightGray))
        return format

        



