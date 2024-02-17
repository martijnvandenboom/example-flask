# Importeer de benodigde modules
from flask import Flask, render_template

# Maak een Flask-applicatie
app = Flask(__name__)

# Definieer een route voor de startpagina
@app.route('/')
def home():
    return 'Welkom op de startpagina van de Flask-webapplicatie!'

# Definieer een route voor een eenvoudige HTML-pagina
@app.route('/pagina')
def pagina():
    return render_template('pagina.html')

# Als dit bestand rechtstreeks wordt uitgevoerd, start dan de app
if __name__ == '__main__':
    app.run(debug=True)