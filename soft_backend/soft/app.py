from flask import Flask

app = Flask(__name__)
app.config["timeout"] = 60  # 60 seconds

@app.route('/')
def hello_world():
    return 'Hello World!'


from show.init import show_blue
from upload.init import upload_blue

app.register_blueprint(show_blue)
app.register_blueprint(upload_blue)

if __name__ == '__main__':
    app.run(port=8080)
