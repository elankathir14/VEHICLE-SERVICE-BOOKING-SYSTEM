from flask import Flask, render_template
from models import init_db
from routes.auth import auth_bp
from routes.booking import booking_bp
from routes.history import history_bp

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "vehicle-service-secret-key"

app.register_blueprint(auth_bp)
app.register_blueprint(booking_bp)
app.register_blueprint(history_bp)


@app.route("/")
def index():
    return render_template("index.html")


init_db()


if __name__ == "__main__":
    app.run(debug=True)
