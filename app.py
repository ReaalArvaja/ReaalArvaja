from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # A simple homepage with a link to the guessing game
    return render_template('index.html')

@app.route('/map')
def map_view():
    # This page shows the interactive map for guessing
    return render_template('map.html')

@app.route('/game')
def game():
    # Render the game page
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)