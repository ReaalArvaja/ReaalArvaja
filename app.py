from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Näitab majaplaani vaadet
    return render_template('index.html')

@app.route('/photosphere/<room>')
def photosphere(room):
    # Näitab konkreetse ruumi fotosfääri
    return render_template('photosphere.html', room=room)

if __name__ == '__main__':
    app.run(debug=True)
