from flask import Blueprint, render_template, session, redirect, url_for
from database import get_db_connection

history_bp = Blueprint("history", __name__)


@history_bp.route("/history")
def history():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    connection = get_db_connection()
    bookings = connection.execute(
        "SELECT * FROM bookings WHERE user_id = ? ORDER BY id DESC",
        (session["user_id"],),
    ).fetchall()
    connection.close()
    return render_template("history.html", bookings=bookings)
