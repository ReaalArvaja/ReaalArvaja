from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # A simple homepage with a link to the guessing game
    return render_template('index.html')

@app.route("/credits")
def credits():
    #hehehehe i did credist page 
    return render_template("credits.html")

@app.route('/game')
def game():
    # Render the game page
    return render_template('game.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)