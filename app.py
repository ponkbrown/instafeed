from flask import Flask, render_template
from flask_script import Manager
from instafeed import recent_media

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return(render_template('index.html', media= recent_media))


if __name__ == "__main__":
    manager.run()
