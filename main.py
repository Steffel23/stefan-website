from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/spiele-hub')
def spiele_hub():
    return render_template('spiele-hub.html')

@app.route('/ueber-mich')
def ueber_mich():
    return render_template('ueber-mich.html')

@app.route('/regelwerk')
def regelwerk():
    return render_template('regelwerk.html')

@app.route('/vorlagen')
def vorlagen():
    return render_template('vorlagen.html')

@app.route('/bot-zentrale')
def bot_zentrale():
    return render_template('bot-zentrale.html')

@app.route('/clicker')
def clicker():
    return render_template('clicker.html')

@app.route('/jump')
def jump():
    return render_template('jump.html')

@app.route('/labyrinth')
def labyrinth():
    return render_template('labyrinth.html')

@app.route('/racing')
def racing():
    return render_template('racing.html')

@app.route('/shooter')
def shooter():
    return render_template('shooter.html')

@app.route('/io')
def io_game():
    return render_template('io.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
