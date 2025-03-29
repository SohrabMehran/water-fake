from flask import Flask, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

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

@app.route('/get-ips', methods=['GET'])
def get_ips():
    conn = sqlite3.connect("ips.db")
    cursor = conn.execute("SELECT ip FROM users")
    ips = [row[0] for row in cursor.fetchall()]
    conn.close()
    return {"ips": ips}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)