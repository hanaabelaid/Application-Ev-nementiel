import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QDateTimeEdit, QHBoxLayout, QMessageBox, QDateEdit,QSizePolicy,QHeaderView
from PyQt5.QtCore import QDate
import mysql.connector
from reportlab.pdfgen import canvas



class ReservationApp(QMainWindow):
    
    def __init__(self):
        super(ReservationApp, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Système de Réservation d\'Événements')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # Widgets pour la réservation d'un événement
        self.label_cne = QLabel('CIN:')
        self.edit_cne = QLineEdit()
        self.edit_cne.setStyleSheet("border: 5px solid rgb(188, 229, 255); border-radius: 20px; padding: 2px;")

        self.label_nom = QLabel('Nom:')
        self.edit_nom = QLineEdit()
        self.edit_nom.setStyleSheet("border: 5px solid rgb(188, 229, 255); border-radius: 20px; padding: 2px;")


        self.label_prenom = QLabel('Prénom:')
        self.edit_prenom = QLineEdit()
        self.edit_prenom.setStyleSheet("border: 5px solid rgb(188, 229, 255); border-radius: 20px; padding: 2px;")


        self.label_telephone = QLabel('Téléphone:')
        self.edit_telephone = QLineEdit()
        self.edit_telephone.setStyleSheet("border: 5px solid rgb(188, 229, 255); border-radius: 20px; padding: 2px;")


        self.label_email = QLabel('Email:')
        self.edit_email = QLineEdit()
        self.edit_email.setStyleSheet("border: 5px solid rgb(188, 229, 255); border-radius: 20px; padding: 2px;")

        
        self.label_date = QLabel("Date de l'événement:")
        self.edit_date = QDateEdit()
        self.edit_date.setStyleSheet("border: 5px solid rgb(188, 229, 255); border-radius: 20px; padding: 2px;")
        self.edit_date.setCalendarPopup(True)
        self.edit_date.setDate(QDate.currentDate())


        self.label_type_pack = QLabel('type du Pack:')
        self.combo_type_pack = QComboBox()
        self.combo_type_pack.setStyleSheet("border: 5px solid rgb(188, 229, 255); border-radius: 20px; padding: 2px;")
        self.fill_combo_type_pack()
        
        
        self.btn_ajouter = QPushButton('Ajouter ')
        self.btn_ajouter.setStyleSheet("background-color: rgb(188, 229, 255);")

        self.btn_ajouter.clicked.connect(self.ajouter_reservation)

        self.btn_supprimer = QPushButton('Supprimer ')
        self.btn_supprimer.setStyleSheet("background-color: rgb(188, 229, 255);")
        self.btn_supprimer.clicked.connect(self.supprimer_reservation)

        self.btn_modifier = QPushButton('Modifier ')
        self.btn_modifier.setStyleSheet("background-color: rgb(188, 229, 255);")
        self.btn_modifier.clicked.connect(self.modifier_reservation)

        self.btn_rechercher = QPushButton('Rechercher ')
        self.btn_rechercher.setStyleSheet("background-color: rgb(188, 229, 255);")
        self.btn_rechercher.clicked.connect(self.rechercher_reservation)

        self.btn_facturer = QPushButton('Facturer')
        self.btn_facturer.setStyleSheet("background-color: rgb(188, 229, 255);")
        self.btn_facturer.clicked.connect(self.generer_facture)

        # Layout pour les boutons
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.btn_ajouter)
        self.button_layout.addWidget(self.btn_supprimer)
        self.button_layout.addWidget(self.btn_modifier)
        self.button_layout.addWidget(self.btn_rechercher)
        self.button_layout.addWidget(self.btn_facturer)

        # Ajouter le layout des boutons au layout principal
        self.layout.addWidget(self.label_cne)
        self.layout.addWidget(self.edit_cne)

        self.layout.addWidget(self.label_nom)
        self.layout.addWidget(self.edit_nom)

        self.layout.addWidget(self.label_prenom)
        self.layout.addWidget(self.edit_prenom)

        self.layout.addWidget(self.label_telephone)
        self.layout.addWidget(self.edit_telephone)

        self.layout.addWidget(self.label_email)
        self.layout.addWidget(self.edit_email)

        self.layout.addWidget(self.label_date)
        self.layout.addWidget(self.edit_date)

        
        self.layout.addWidget(self.label_type_pack)
        self.layout.addWidget(self.combo_type_pack)

        self.layout.addLayout(self.button_layout)

        # Créer le tableau ici
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['CNE', 'Nom', 'Prénom', 'Téléphone', 'Email', 'Date',  'type Pack'])
        self.layout.addWidget(self.table)

        self.central_widget.setLayout(self.layout)
        tableSizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.setSizePolicy(tableSizePolicy)

        # Définir la largeur des colonnes pour occuper tout l'espace
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Appliquer le layout principal à la fenêtre
        self.central_widget.setLayout(self.layout)

        self.populate_table()
        
###########################################################################

    def populate_table(self):
        server = 'localhost'
        database = 'traiteur'
        username = 'root'
        password = ''

        try:
            con = mysql.connector.connect(
                host=server,
                user=username,
                password=password,
                database=database
            )
            cursordb = con.cursor()

            # Fetch data a partir du tableau client
            sql = "SELECT CNE, nom, prenom, tele, email, date, type_event FROM client"
            cursordb.execute(sql)
            data = cursordb.fetchall()

            # Remplissage la table avec les données récupérées
            self.table.setRowCount(len(data))
            for row_num, row_data in enumerate(data):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.table.setItem(row_num, col_num, item)


            con.close()

        except mysql.connector.Error as err:
            print("Error:", err)
            
###########################################################################
    def fill_combo_type_pack(self):
        try:
            
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='traiteur'
            )
            cursordb = con.cursor()

            # Sélectionnement toutes les valeurs type_event dans la table des événements
            query_select_events = "SELECT type_event FROM event"
            cursordb.execute(query_select_events)
            result = cursordb.fetchall()

            # Effacer les éléments existants dans la zone de liste
            self.combo_type_pack.clear()

            # Ajouter des éléments du résultat de la requête à la zone de liste
            for row in result:
                self.combo_type_pack.addItem(row[0])
            con.close()

        except Exception as e:
            QMessageBox.warning(self, 'Erreur', f'Erreur lors de la récupération des types d\'événement : {str(e)}')
            
###########################################################################

    def ajouter_reservation(self):
        cne = self.edit_cne.text()
        nom = self.edit_nom.text()
        prenom = self.edit_prenom.text()
        telephone = self.edit_telephone.text()
        email = self.edit_email.text()
        date = self.edit_date.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        type_pack = self.combo_type_pack.currentText()

        if cne and nom and prenom and telephone and email and date:
            try:

                con = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='traiteur'
                )
                cursordb = con.cursor()

                # vérifie si le type_event sélectionné existe dans la table des événements
                selected_event = self.combo_type_pack.currentText()
                query_check_event = "SELECT type_event FROM event WHERE type_event = %s"
                cursordb.execute(query_check_event, (selected_event,))
                result = cursordb.fetchone()

                if not result:
                    QMessageBox.warning(self, 'Erreur', 'Le type d\'événement sélectionné n\'existe pas dans la table event.')
                    return

                # Inserer les information deans la table client
                query_insert_reservation = "INSERT INTO client (CNE, nom, prenom, tele, email, type_event, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values_reservation = (cne, nom, prenom, telephone, email, selected_event, date)
                cursordb.execute(query_insert_reservation, values_reservation)

                con.commit()
                con.close()

                # Mettre à jour le tableau dans GUI
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(cne))
                self.table.setItem(row_position, 1, QTableWidgetItem(nom))
                self.table.setItem(row_position, 2, QTableWidgetItem(prenom))
                self.table.setItem(row_position, 3, QTableWidgetItem(telephone))
                self.table.setItem(row_position, 4, QTableWidgetItem(email))
                self.table.setItem(row_position, 5, QTableWidgetItem(date))
                self.table.setItem(row_position, 6, QTableWidgetItem(selected_event))
                self.clear_inputs()

            except Exception as e:
                QMessageBox.warning(self, 'Erreur', f'Erreur lors de l\'ajout dans la base de données : {str(e)}')

        else:
            QMessageBox.warning(self, 'Attention', 'Veuillez remplir tous les champs.')

############################################################################
    def supprimer_reservation(self):
        cne_to_delete = self.edit_cne.text()

        try:

            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='traiteur'
            )
            cursordb = con.cursor()

            # Supprimer la réservation de la table client
            query_delete_reservation = "DELETE FROM client WHERE CNE = %s"
            cursordb.execute(query_delete_reservation, (cne_to_delete,))


            con.commit()
            con.close()

            # Mettre à jour le tableau dans GUI
            self.remove_row_by_cne(cne_to_delete)

        except Exception as e:
            QMessageBox.warning(self, 'Erreur', f'Erreur lors de la suppression dans la base de données : {str(e)}')

###########################################################################

    def remove_row_by_cne(self, cne):
        # Itérer à travers les lignes de la table
        for row in range(self.table.rowCount()):
            # Si une correspondance est trouvée, supprimer la ligne et sortir de la boucle
            if self.table.item(row, 0).text() == cne:
                self.table.removeRow(row)
                break


############################################################################

    def modifier_reservation(self):
        id_to_modify = self.edit_cne.text()

        try:

            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='traiteur'
            )
            cursordb = con.cursor()

            # Vérifiez si CNE existe dans la table client
            query_check_id = "SELECT CNE FROM client WHERE CNE = %s"
            cursordb.execute(query_check_id, (id_to_modify,))
            result = cursordb.fetchone()

            if not result:
                QMessageBox.warning(self, 'Erreur', 'L\'ID spécifié n\'existe pas dans la table client.')
                return

            #Obtenir les informations pour la modification
            cne = self.edit_cne.text()
            nom = self.edit_nom.text()
            prenom = self.edit_prenom.text()
            telephone = self.edit_telephone.text()
            email = self.edit_email.text()
            date = self.edit_date.dateTime().toString("yyyy-MM-dd HH:mm:ss")
            type_pack = self.combo_type_pack.currentText()

            # Mettre à jour la réservation dans la table client
            query_update_reservation = "UPDATE client SET nom = %s, prenom = %s, tele = %s, email = %s, type_event = %s, date = %s WHERE CNE = %s"
            values_update_reservation = (nom, prenom, telephone, email, type_pack, date, id_to_modify)
            cursordb.execute(query_update_reservation, values_update_reservation)


            con.commit()
            con.close()

        except Exception as e:
            QMessageBox.warning(self, 'Erreur', f'Erreur lors de la modification dans la base de données : {str(e)}')
###########################################################################
    def rechercher_reservation(self):
        cne = self.edit_cne.text()
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0).text() == cne:
                self.table.selectRow(row)
                return
        QMessageBox.warning(self, 'Attention', 'Aucune réservation trouvée pour le CNE spécifié.')
        
###########################################################################
    def generer_facture(self):
        selected_row = self.table.currentRow()

        if selected_row >= 0:
            try:
                # assumer les colonne dans la table
                cne_client = self.table.item(selected_row, 0).text()
                type_pack = self.table.item(selected_row, 6).text()


                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='traiteur'
                )
                cursor = connection.cursor()

                # Exécutez la requête pour obtenir le prix du type de pack et les informations du client
                cursor.execute("""
                    SELECT c.nom, c.prenom, e.type_event, e.prix
                    FROM client c
                    JOIN event e ON c.type_event = e.type_event
                    WHERE c.CNE = %s
                """, (cne_client,))

                result = cursor.fetchone()

                if result:
                    nom_client, prenom_client, type_pack, prix_pack = result

                    # Générer une facture PDF à l'aide de la bibliotheque reportlab
                    pdf_filename = f'invoice_{type_pack}_{cne_client}.pdf'
                    c = canvas.Canvas(pdf_filename)
                    
                    # Titre
                    c.setFont("Helvetica-Bold", 16)
                    c.drawString(100, 750, 'Facture')
                    c.line(100, 745, 500, 745)

                    # informations de client
                    c.setFont("Helvetica", 12)
                    c.drawString(100, 720, f'Client: {nom_client} {prenom_client} ({cne_client})')
                    c.line(100, 715, 500, 715)

                    # Invoice details
                    c.drawString(100, 690, f'Type du pack choisi: {type_pack}')
                    c.drawString(100, 670, f'Prix du pack: {prix_pack}')

                    c.line(100, 665, 500, 665)


                    c.save()

                    QMessageBox.information(self, 'Facture', f'Facture générée avec succès. Voir {pdf_filename}')
                else:
                    QMessageBox.warning(self, 'Erreur', 'Informations non trouvées pour le type de pack sélectionné.')
            except mysql.connector.Error as e:
                QMessageBox.warning(self, 'Erreur', f'Erreur de base de données : {str(e)}')
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        else:
            QMessageBox.warning(self, 'Attention', 'Veuillez sélectionner une réservation pour générer la facture.')

###########################################################################

    def clear_inputs(self):
        self.edit_cne.clear()
        self.edit_nom.clear()
        self.edit_prenom.clear()
        self.edit_telephone.clear()
        self.edit_email.clear()
        self.edit_date.clear()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReservationApp()
    window.show()
    sys.exit(app.exec_())
