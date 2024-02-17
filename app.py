from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render de hoofdpagina met een link naar pagina.html
    return render_template('index.html')

@app.route('/pagina')
def pagina():
    # Render de pagina.html
    return render_template('pagina.html')

if __name__ == '__main__':
    app.run(debug=True)
