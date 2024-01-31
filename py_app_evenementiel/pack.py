import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QDialog, QScrollArea, QHBoxLayout,QGroupBox, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import mysql.connector

class pack_evenements(QWidget):
    def __init__(self):
        super().__init__()

        self.pack_evenements = self.creer_pack_evenements()
        self.selected_event_index = None

        main_layout = QVBoxLayout()

        # Créer une zone de défilement pour les événements
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Widget qui contiendra les étiquettes des événements
        events_widget = QWidget()
        scroll_area.setWidget(events_widget)

        # Layout pour les événements
        events_layout = QVBoxLayout(events_widget)
        events_layout.setObjectName("events_layout")
        
        main_layout.addWidget(scroll_area)


        # Bouton pour ajouter un événement
        self.add_button = QPushButton("Ajouter un événement")
        self.add_button.clicked.connect(self.ajouter_evenement)
        self.add_button.setStyleSheet("background-color: rgb(188, 229, 255);")
        main_layout.addWidget(self.add_button)

        # Bouton pour supprimer un événement sélectionné
        self.remove_button = QPushButton("Supprimer l'événement sélectionné")
        self.remove_button.clicked.connect(self.supprimer_evenement_selectionne)
        self.remove_button.setStyleSheet("background-color: rgb(188, 229, 255);")
        main_layout.addWidget(self.remove_button) 

        self.setLayout(main_layout)

        self.actualiser_affichage()

        self.setWindowTitle('Interface Pack Evenements')
        self.show()

###########################################################################

    def creer_evenement(self, type_event, prix, descrip):
        return Evenement(type_event, prix, descrip)

    def creer_pack_evenements(self):
        try:
            # Ouvrir une connexion à la base de données
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='traiteur'
            )
            cursordb = con.cursor()

            # Récupérer les données de la table event
            query_select_events = "SELECT type_event, prix, descrip FROM event"
            cursordb.execute(query_select_events)
            result = cursordb.fetchall()

            evenements = []

            # Créer des objets Evenement à partir des données de la base de données
            for type_event, prix, descrip in result:
                evenement = self.creer_evenement(type_event, prix, descrip)
                evenements.append(evenement)


            con.close()

            return PackEvenements("Nom du pack", 0.0, evenements)
            

        except Exception as e:
            # En cas d'erreur, afficher un avertissement
            QMessageBox.warning(self, 'Erreur', f'Erreur lors de la récupération des événements : {str(e)}')
            return PackEvenements("Nom du pack par défaut", 0.0, [])

###########################################################################

    def ajouter_evenement(self):
        # Ouvrir une boîte de dialogue pour obtenir les informations sur l'événement
        dialog = AjoutEvenementDialog(self)
        if dialog.exec_() == QDialog.Accepted:

            type_event, prix, descrip = dialog.obtenir_informations_evenement()
            evenement = self.creer_evenement(type_event, prix, descrip)
            self.pack_evenements.ajouter_evenement(evenement)
            # Vérifier si les informations nécessaires sont présentes
            if type_event and prix and descrip:
                try:
                    con = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='',
                        database='traiteur'
                    )
                    cursordb = con.cursor()

                    # Insérer l'événement dans la table 'event' de la base de données
                    query_insert_event = "INSERT INTO event (type_event, prix, descrip) VALUES (%s, %s, %s)"
                    values_event = (type_event, prix, descrip)
                    cursordb.execute(query_insert_event, values_event)

                    con.commit()
                    con.close()

                    self.actualiser_affichage()

                except Exception as e:
                    # En cas d'erreur, afficher un avertissement
                    QMessageBox.warning(self, 'Erreur', f'Erreur lors de l\'ajout dans la base de données : {str(e)}')


###########################################################################

    def supprimer_evenement_selectionne(self):
        if self.selected_event_index is not None:
            try:
                con = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='traiteur'
                )
                cursordb = con.cursor()

                # Obtenez l'ID de l'événement sélectionné
                selected_event = self.pack_evenements.evenements[self.selected_event_index]

                query_delete_event = "DELETE FROM event WHERE type_event = %s AND prix = %s AND descrip = %s"
                values_event = (selected_event.type_event, selected_event.prix, selected_event.descrip)
                cursordb.execute(query_delete_event, values_event)

                con.commit()
                con.close()

                self.pack_evenements.supprimer_evenement(self.selected_event_index)
                self.selected_event_index = None
                self.actualiser_affichage()

            except Exception as e:
                QMessageBox.warning(self, 'Erreur', f'Erreur lors de la suppression dans la base de données : {str(e)}')

###########################################################################

    def selectionner_evenement(self, index):
        if self.selected_event_index is not None:
            ancienne_label = self.findChild(QLabel, f"event_label_{self.selected_event_index}")
            if ancienne_label:
                ancienne_label.setStyleSheet("")

        self.selected_event_index = index

        nouvel_label = self.findChild(QLabel, f"event_label_{self.selected_event_index}")
        if nouvel_label:
            nouvel_label.setStyleSheet("background-color: lightblue;")
            
###########################################################################

    def actualiser_affichage(self):
        events_layout = self.findChild(QVBoxLayout, name="events_layout")
        if events_layout is not None:
            for i in reversed(range(events_layout.count())):
                widget = events_layout.itemAt(i).widget()
                if widget:
                    widget.setParent(None)

        for index, evenement in enumerate(self.pack_evenements.evenements):
            event_label = QLabel(f"- {evenement.type_event} (Prix: {evenement.prix} DHs)")
            descrip_label = QLabel(f"  {evenement.descrip}")
            event_label.setObjectName(f"event_label_{index}")
            event_label.mousePressEvent = lambda event, i=index: self.selectionner_evenement(i)
            events_layout.addWidget(event_label)
            events_layout.addWidget(descrip_label)

###########################################################################

class Evenement:
    def __init__(self, type_event, prix, descrip):
        self.type_event = type_event
        self.descrip = descrip
        self.prix=prix

###########################################################################
class PackEvenements:
    def __init__(self, type_event, prix, evenements):
        self.type_event = type_event
        self.prix = prix
        self.evenements = evenements

    def ajouter_evenement(self, evenement):
        self.evenements.append(evenement)

    def supprimer_evenement(self, index):
        if 0 <= index < len(self.evenements):
            del self.evenements[index]

###########################################################################
class AjoutEvenementDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Ajouter un événement")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.nom_edit = QLineEdit(self)
        self.prix_edit = QLineEdit(self)
        self.descrip_edit = QTextEdit(self)

        layout.addWidget(QLabel("Nom de l'événement:"))
        layout.addWidget(self.nom_edit)

        layout.addWidget(QLabel("Prix de l'événement:"))
        layout.addWidget(self.prix_edit)

        layout.addWidget(QLabel("Description de l'événement:"))
        layout.addWidget(self.descrip_edit)

        buttons_layout = QHBoxLayout()

        ajouter_button = QPushButton("Ajouter", self)
        ajouter_button.clicked.connect(self.accept)
        buttons_layout.addWidget(ajouter_button)

        annuler_button = QPushButton("Annuler", self)
        annuler_button.clicked.connect(self.reject)
        buttons_layout.addWidget(annuler_button)

        layout.addLayout(buttons_layout)

        self.setLayout(layout)
        
###########################################################################

    def obtenir_informations_evenement(self):
        type_event = self.nom_edit.text()
        prix_text = self.prix_edit.text()
        descrip = self.descrip_edit.toPlainText()

        try:
            prix = float(prix_text)
        except ValueError:
            prix = 0.0

        return type_event, prix, descrip





