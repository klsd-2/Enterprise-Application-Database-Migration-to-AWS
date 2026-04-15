from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

@app.route("/")
def home():
    return jsonify({"message": "Enterprise App Running on AWS 🚀"})

@app.route("/data")
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({"db_time": str(result[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
