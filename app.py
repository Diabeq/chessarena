from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Działa z Rendera!"

# WAŻNE: NIE dodawaj "if __name__ == '__main__'" na Renderze
