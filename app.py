from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage (resets on restart)
bookings = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book-ticket")
def book_ticket():
    return render_template("book.html")

@app.route("/submit-booking", methods=["POST"])
def submit_booking():
    name = request.form["name"]
    train = request.form["train"]
    date = request.form["date"]
    seat = request.form["seat"]

    booking = {
        "name": name,
        "train": train,
        "date": date,
        "seat": seat
    }

    bookings.append(booking)

    return render_template("index.html", message="Ticket booked successfully!")

@app.route("/view-bookings")
def view_bookings():
    return render_template("bookings.html", bookings=bookings)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
