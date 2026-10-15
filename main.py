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

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

@app.route('/bot-config')
def bot_config():
    return render_template('bot-config.html')

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

# HIER IST DEINE NEUE ROUTE FÜR DAS FROSCH-SPIEL!
@app.route('/frosch')
def frosch():
    return render_template('frosch.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
