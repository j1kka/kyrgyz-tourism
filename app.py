from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hotels")
def hotels():
    hotels_data = [
        {"name": "Hotel Asia", "location": "Bishkek", "stars": 4},
        {"name": "Plaza Hotel", "location": "Osh", "stars": 5},
        {"name": "Rixos Hotel", "location": "Issyk-Kul", "stars": 5},
        {"name": "Guesthouse Kyrgyzstan", "location": "Naryn", "stars": 3}
    ]
    return render_template("hotels.html", hotels=hotels_data)

@app.route("/transport")
def transport():
    transport_data = [
        {"type": "Taxi", "city": "Bishkek", "info": "Средняя стоимость: 200-400 KGS"},
        {"type": "Bus", "city": "Osh", "info": "Маршрутки и автобусы по всему городу"},
        {"type": "Airport Shuttle", "city": "Bishkek", "info": "Связь с международным аэропортом"}
    ]
    return render_template("transport.html", transports=transport_data)

@app.route("/reviews")
def reviews():
    reviews_data = [
        {"user": "Alice", "comment": "Beautiful country, very friendly people!", "place": "Issyk-Kul"},
        {"user": "Bob", "comment": "Hotels were clean and comfortable.", "place": "Bishkek"},
        {"user": "Charlie", "comment": "Transport is cheap and reliable.", "place": "Osh"}
    ]
    return render_template("reviews.html", reviews=reviews_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
