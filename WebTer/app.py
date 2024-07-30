from flask import Flask, jsonify
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Terminal Button</title>
        <style>
            .button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                color: white;
                background-color: #007BFF;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <button class="button" onclick="startTerminal()">Start Terminal</button>
        <script>
            function startTerminal() {
                fetch('/start-terminal')
                    .then(response => response.json())
                    .then(data => alert(data.message))
                    .catch(error => console.error('Error:', error));
            }
        </script>
    </body>
    </html>
    '''

@app.route('/start-terminal')
def start_terminal():
    try:
        if sys.platform == "win32":
            # Command to open Command Prompt
            subprocess.Popen('start cmd', shell=True)
            # Command to open PowerShell
            # subprocess.Popen('start powershell', shell=True)
        else:
            # Command for Linux (you can add MacOS support similarly)
            subprocess.Popen(['gnome-terminal'])  # For GNOME Terminal
            # subprocess.Popen(['xterm'])  # For Xterm
        return jsonify({'message': 'Terminal started successfully!'})
    except Exception as e:
        return jsonify({'message': f'Failed to start terminal: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
