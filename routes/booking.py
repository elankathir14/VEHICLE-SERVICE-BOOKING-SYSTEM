from flask import Blueprint, render_template, request, redirect, url_for, session
from database import get_db_connection

booking_bp = Blueprint("booking", __name__)


@booking_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template("dashboard.html", username=session["username"])


@booking_bp.route("/booking", methods=["GET", "POST"])
def booking():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        vehicle_type = request.form["vehicle_type"]
        service_type = request.form["service_type"]
        booking_date = request.form["booking_date"]
        notes = request.form.get("notes", "")

        connection = get_db_connection()
        connection.execute(
            "INSERT INTO bookings (user_id, vehicle_type, service_type, booking_date, notes) VALUES (?, ?, ?, ?, ?)",
            (session["user_id"], vehicle_type, service_type, booking_date, notes),
        )
        connection.commit()
        connection.close()
        return redirect(url_for("history.history"))

    return render_template("booking.html")
