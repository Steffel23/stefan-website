from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='templates')

@app.route('/avatar.png')
def custom_avatar():
    if os.path.exists('avatar.png'):
        return send_from_directory('.', 'avatar.png')
    elif os.path.exists('templates/avatar.png'):
        return send_from_directory('templates', 'avatar.png')
    return send_from_directory('.', 'avatar.png')

@app.route('/')
def home():
    # ULTIMATIVER FIX: Sucht die index.html überall, damit nie wieder ein Fehler kommt!
    if os.path.exists('templates/index.html'):
        return render_template('index.html')
    elif os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    return "Startseite nicht gefunden! Bitte stelle sicher, dass eine index.html existiert."

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
