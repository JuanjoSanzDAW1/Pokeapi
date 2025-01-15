import os
import subprocess


def run_command(command, get_output=False):
    if get_output:
        return subprocess.check_output(command, shell=True, text=True)
    else:
        subprocess.run(command, shell=True, check=True)


def install_dependencies():
    print("Ahora se intalan las dependencias deberia estar instalado creo")
    run_command("sudo apt update")
    run_command("sudo apt install -y python3 python3-pip python3-venv nginx")


def setup_flask_app():
    print("Aqui ahora empieza la config de FLASK")
    app_dir = '/var/www/pokemon_app'

    run_command(f"sudo mkdir -p {app_dir}")
    os.chdir(app_dir)

    run_command("python3 -m venv venv")

    run_command("./venv/bin/pip install Flask gunicorn")

    create_flask_app_files(app_dir)

    run_command(f"sudo ./venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 app:app")


def create_flask_app_files(app_dir):
    app_code = '''from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello_world')
def hello_world():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)
    '''

    with open(os.path.join(app_dir, 'app.py'), 'w') as f:
        f.write(app_code)


    os.makedirs(os.path.join(app_dir, 'templates'), exist_ok=True)


    index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index Page</title>
    <link  rel="stylesheet" href="static/styles.css">
</head>
<body>
    <h1>Welcome to the Pokemon App</h1>
    <button id="helloWorldButton">Go to Hello World</button>
    <p id="response"></p>
    <script>
        document.getElementById("helloWorldButton").addEventListener("click", function() {
            fetch('/hello_world')
                .then(response => response.json())
                .then(data => {
                    document.getElementById("response").innerText = data.message;
                })
                .catch(error => console.log('Error:', error));
        });
    </script>
</body>
</html>
'''

    with open(os.path.join(app_dir, 'templates', 'index.html'), 'w') as f:
        f.write(index_html)


    os.makedirs(os.path.join(app_dir, 'static'), exist_ok=True)


    css_code = '''body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin-top: 50px;
}

button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

#response {
    margin-top: 20px;
    font-size: 18px;
    color: #333;
}
'''
    with open(os.path.join(app_dir, 'static', 'styles.css'), 'w') as f:
        f.write(css_code)


def configure_nginx():
    print("Aqui ahora toca nginx")
    nginx_config = '''
server {
    listen 80;
    server_name tu_ip;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
'''
    nginx_config_path = '/etc/nginx/sites-available/pokemon_app'
    with open(nginx_config_path, 'w') as f:
        f.write(nginx_config)

    run_command(f"sudo ln -s {nginx_config_path} /etc/nginx/sites-enabled/")

    run_command("sudo nginx -t")

    run_command("sudo systemctl reload nginx")


if __name__ == '__main__':
    install_dependencies()
    setup_flask_app()
    configure_nginx()