from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hotels")
def hotels():
    hotels = [
        {"name": "Hyatt Regency Bishkek", "city": "Bishkek", "price": "$120", "rating": "5★"},
        {"name": "Plaza Hotel Bishkek", "city": "Bishkek", "price": "$70", "rating": "4★"},
        {"name": "Karagat Hotel", "city": "Issyk-Kul", "price": "$50", "rating": "4★"},
        {"name": "Sunrise Guest House", "city": "Karakol", "price": "$30", "rating": "3★"},
    ]
    return render_template("hotels.html", hotels=hotels)

@app.route("/transport")
def transport():
    transport = [
        {"type": "Namba Taxi", "price": "100–300 KGS"},
        {"type": "Yandex Go", "price": "120–350 KGS"},
        {"type": "Marshrutka", "price": "20–50 KGS"},
        {"type": "Intercity Taxi", "price": "500–800 KGS"},
    ]
    return render_template("transport.html", transport=transport)

@app.route("/reviews")
def reviews():
    reviews = [
        {"user": "Anna", "text": "Amazing nature and friendly people!", "rating": "5/5"},
        {"user": "John", "text": "Cheap transport and good hotels.", "rating": "4/5"},
        {"user": "Aida", "text": "Issyk-Kul is beautiful!", "rating": "5/5"},
    ]
    return render_template("reviews.html", reviews=reviews)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
