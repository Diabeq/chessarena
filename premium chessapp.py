from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        player = request.form.get('player_name')
        return redirect(url_for('lobby', player=player))
    return render_template('menu.html')

@app.route('/lobby')
def lobby():
    player = request.args.get('player', 'anonim')
    is_admin = player.lower() == 'admin'
    return render_template('lobby.html', player=player, is_admin=is_admin)

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)
