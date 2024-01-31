import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import mysql.connector
import calendar

class Home(QMainWindow):
    def __init__(self):
        super().__init__()

        # BienvenueApp initialization
        bienvenue_label = QLabel('Bienvenue sur app GestEvent', self)
        bienvenue_label.setStyleSheet('font-size: 25px; color: #333; font-weight: bold;')

        bienvenue_layout = QVBoxLayout()
        bienvenue_layout.addWidget(bienvenue_label)

        # Create bienvenue_widget
        bienvenue_widget = QWidget()
        bienvenue_widget.setLayout(bienvenue_layout)
        bienvenue_widget.setFixedHeight(100)

        # MainWindow initialization
        self.figure, (self.ax_stem, self.ax_bar) = plt.subplots(1, 2, sharey=False)
        self.canvas = FigureCanvas(self.figure)

        # Combine BienvenueApp and MainWindow widgets in a vertical layout
        combined_layout = QVBoxLayout()
        combined_layout.addWidget(bienvenue_widget)
        combined_layout.addWidget(self.canvas)

        combined_widget = QWidget()
        combined_widget.setLayout(combined_layout)

        self.setCentralWidget(combined_widget)

        # Set window properties
        self.setGeometry(600, 600, 1200, 600)  # Adjusted width and height
        self.setWindowTitle('Bienvenue et Diagrammes App')

        # Fetch and update plots from the database
        self.update_plots_from_database()

    def update_plots_from_database(self):
        # Replace these credentials with your MySQL server details
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='traiteur'
        )

        # Fetch data for stem plot
        query_stem = """
        SELECT EXTRACT(MONTH FROM date) AS month, SUM(prix) AS revenue
        FROM client
        JOIN event ON client.type_event = event.type_event
        GROUP BY month
        ORDER BY month;
        """

        # Execute the query and fetch the results into a list of tuples
        cursor_stem = connection.cursor()
        cursor_stem.execute(query_stem)
        results_stem = cursor_stem.fetchall()

        # Close the database connection
        connection.close()

        # Extract months and revenue from the list of tuples for stem plot
        months_stem, revenue_stem = zip(*results_stem)

        # Calculate the total revenue for stem plot
        total_revenue_stem = sum(revenue_stem)

        # Calculate the percentage of revenue for each month for stem plot
        percentages_stem = [(r / total_revenue_stem) * 100 for r in revenue_stem]

        # Convert numeric months to abbreviated month names for stem plot
        month_names_stem = [calendar.month_abbr[int(month)] for month in months_stem]

        # Update the Matplotlib stem plot
        self.ax_stem.clear()
        self.ax_stem.stem(month_names_stem, percentages_stem, linefmt='b-', markerfmt='bo', basefmt='r-')
        self.ax_stem.set_ylabel('Pourcentage de Revenu')
        self.ax_stem.set_title('Pourcentage de Revenu par Mois')

        # Fetch data for bar plot
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='traiteur'
        )

        # Assuming 'client' is the table name in your database for bar plot
        query_bar = "SELECT EXTRACT(MONTH FROM date) AS month, COUNT(*) AS client_frequency FROM client GROUP BY month ORDER BY month;"

        # Execute the query and fetch the results into a list of tuples
        cursor_bar = connection.cursor()
        cursor_bar.execute(query_bar)
        results_bar = cursor_bar.fetchall()

        # Close the database connection
        connection.close()

        # Extract months and client frequencies from the list of tuples for bar plot
        months_bar, client_frequencies_bar = zip(*results_bar)

        # Convert numeric months to abbreviated month names for bar plot
        month_names_bar = [calendar.month_abbr[int(month)] for month in months_bar]

        # Update the Matplotlib bar plot
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
