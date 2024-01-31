import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import mysql.connector
import calendar

class Home(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialisation du label
        bienvenue_label = QLabel('Bienvenue sur app GestEvent', self)
        bienvenue_label.setStyleSheet('font-size: 25px; color: #333; font-weight: bold;')

        bienvenue_layout = QVBoxLayout()
        bienvenue_layout.addWidget(bienvenue_label)

        # Créer bienvenue_widget
        bienvenue_widget = QWidget()
        bienvenue_widget.setLayout(bienvenue_layout)
        bienvenue_widget.setFixedHeight(100)

        # MainWindow initialization
        self.figure, (self.ax_stem, self.ax_bar) = plt.subplots(1, 2, sharey=False)
        self.canvas = FigureCanvas(self.figure)

        # Combinez les widgets HOME et MainWindow dans une disposition verticale
        combined_layout = QVBoxLayout()
        combined_layout.addWidget(bienvenue_widget)
        combined_layout.addWidget(self.canvas)

        combined_widget = QWidget()
        combined_widget.setLayout(combined_layout)

        self.setCentralWidget(combined_widget)

        self.setGeometry(600, 600, 1200, 600)  # Adjusted width and height
        self.setWindowTitle('Bienvenue et Diagrammes App')

        # Récupérer et mettre à jour pour des diagrammes
        self.update_plots_from_database()

    def update_plots_from_database(self):
        
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='traiteur'
        )

        #  Récupérer les données pour le tracé les diagrammes
        query_stem = """
        SELECT EXTRACT(MONTH FROM date) AS month, SUM(prix) AS revenue
        FROM client
        JOIN event ON client.type_event = event.type_event
        GROUP BY month
        ORDER BY month;
        """

        #Exécutez la requête et récupérez les résultats
        cursor_stem = connection.cursor()
        cursor_stem.execute(query_stem)
        results_stem = cursor_stem.fetchall()

        # Close the database connection
        connection.close()

        # Extraire les mois et les revenus
        months_stem, revenue_stem = zip(*results_stem)

        # Calculer le revenu total
        total_revenue_stem = sum(revenue_stem)

        # Calculer le pourcentage de revenus pour chaque mois
        percentages_stem = [(r / total_revenue_stem) * 100 for r in revenue_stem]

        # Convertir les mois numériques en noms de mois
        month_names_stem = [calendar.month_abbr[int(month)] for month in months_stem]

        # Mettre à jour le diagramme
        self.ax_stem.clear()
        self.ax_stem.stem(month_names_stem, percentages_stem, linefmt='b-', markerfmt='bo', basefmt='r-')
        self.ax_stem.set_ylabel('Pourcentage de Revenu')
        self.ax_stem.set_title('Pourcentage de Revenu par Mois')


        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='traiteur'
        )

        #assumer la table client dans la base de donnee
        query_bar = "SELECT EXTRACT(MONTH FROM date) AS month, COUNT(*) AS client_frequency FROM client GROUP BY month ORDER BY month;"

        # Exécutez la requête et récupérez les résultats
        cursor_bar = connection.cursor()
        cursor_bar.execute(query_bar)
        results_bar = cursor_bar.fetchall()

        connection.close()

        #Extraire les mois et les fréquences des clients
        months_bar, client_frequencies_bar = zip(*results_bar)

        # Convertir les mois numériques en noms de mois
        month_names_bar = [calendar.month_abbr[int(month)] for month in months_bar]

        # UMettre à jour le tracé
        self.ax_bar.clear()
        self.ax_bar.bar(month_names_bar, client_frequencies_bar, color=(153/255, 205/255, 232/255))
        self.ax_bar.set_xlabel('Mois')
        self.ax_bar.set_ylabel('Nombre des Clients')
        self.ax_bar.set_title('Nombre des Clients par mois')

        # Redraw the canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    home_app = Home()
    home_app.show()
    sys.exit(app.exec_())
