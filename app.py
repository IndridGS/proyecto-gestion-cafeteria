from flask import Flask
from models import db as database
from views.main import main_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database.init_app(app)

app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
