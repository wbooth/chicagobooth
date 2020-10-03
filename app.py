import yaml
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    with open('data/resources.yml', 'r') as file:
        resources = yaml.load(file)
    return render_template('home.html', title='Home', resources=resources)


if __name__ == '__main__':
    app.run()
