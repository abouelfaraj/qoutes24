# myapp/front/app.py
from flask import Flask
from routes.routes import routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if __name__ == "__main__":
    app.run(debug=True)
