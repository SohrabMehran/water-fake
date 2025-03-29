from flask import Flask, request
from flask_cors import CORS  # اینو اضافه کن
import sqlite3

app = Flask(__name__)
CORS(app)  # این CORS رو فعال می‌کنه

# ساخت دیتابیس
conn = sqlite3.connect("ips.db")
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT)")
conn.close()

@app.route('/log-ip', methods=['POST'])
def log_ip():
    ip = request.json['ip']
    conn = sqlite3.connect("ips.db")
    conn.execute("INSERT INTO users (ip) VALUES (?)", (ip,))
    conn.commit()
    conn.close()
    return "IP stored!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)