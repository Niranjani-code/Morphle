from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Niranjani"
    username = os.getenv("USER", "unknown")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)

