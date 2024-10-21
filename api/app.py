from flask import Flask
from flask_cors import CORS
from api.routes import app as routes_app

app = Flask(__name__)
CORS(app)  

app.register_blueprint(routes_app)

if __name__ == '__main__':
    app.run(debug=True)
