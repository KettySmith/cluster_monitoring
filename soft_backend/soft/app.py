import flask_cors
from flask import Flask

from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config["timeout"] = 60  # 60 seconds
flask_cors.CORS(app, supports_credentials=True, resources=r"/*")
@app.route('/')
def hello_world():
    return 'Hello World!'


from show.init import show_blue
from upload.init import upload_blue
from search.init import search_blue

app.register_blueprint(show_blue)
app.register_blueprint(upload_blue)
app.register_blueprint(search_blue)

if __name__ == '__main__':
    app.run(port=8090)
