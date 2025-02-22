from flask import Flask, render_template_string
import subprocess
import datetime
import os
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    full_name = "Your Full Name"  # Replace with your full name

    # System username
    username = os.getlogin()

    # Server time in IST
    ist_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')

    # Top command output
    top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout

    # HTML template to display the data
    html_template = """
    <h1>HTOP Endpoint</h1>
    <p><strong>Name:</strong> {{ full_name }}</p>
    <p><strong>Username:</strong> {{ username }}</p>
    <p><strong>Server Time (IST):</strong> {{ ist_time }}</p>
    <h2>Top Output</h2>
    <pre>{{ top_output }}</pre>
    """

    return render_template_string(html_template, full_name=full_name, username=username, ist_time=ist_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)