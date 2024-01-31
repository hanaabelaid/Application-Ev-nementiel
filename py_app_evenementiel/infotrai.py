from PyQt5.QtWidgets import  QLabel, QVBoxLayout
from PyQt5.QtWidgets import QWidget
class InfoTraiteurApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        email_label = QLabel('Email: GestEvent@gmail.com', self)
        traiteur_label = QLabel('Traiteur: GestEvent', self)
        adresse_label = QLabel('Adresse: Boulevard , Tanger', self)
        num_label = QLabel('Numéro_Téléphone: 06-88-29-11-12', self)
        insta_label = QLabel('instagrame: traiteur_GestEvent', self)
        site_label = QLabel('Site Web : www.GestEvent.com', self)
        Tarifs_label = QLabel('Tarifs : Varient en fonction du type de pack choisi', self)
        Cuisine_label = QLabel('Spécialités Culinaires : Cuisine française raffinée, cuisine marocaine.', self)
        
                
        

        layout = QVBoxLayout()
        
        layout.addWidget(email_label)
        layout.addWidget(traiteur_label)
        layout.addWidget(adresse_label)
        layout.addWidget(num_label)
        layout.addWidget(insta_label)
        layout.addWidget(site_label)
        layout.addWidget(Tarifs_label)
        layout.addWidget(Cuisine_label)

        self.setLayout(layout)

        self.setGeometry(400, 400, 800, 400)  # Even larger window size for InfoTraiteurApp
        self.setWindowTitle('Info Traiteur App')
        self.setStyleSheet('''
            QLabel {
                font-size: 20px;
                color: #333;
                margin-bottom: 8px;
            }
            QWidget {
                background-color: #f8f8f8;
                border: 1px solid #ccc;
                border-radius: 30px;
                padding: 10px;
            }
        ''')
