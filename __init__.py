from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel
from flask_login import LoginManager
from flask_change_password import ChangePassword

app = Flask(__name__)
app.secret_key = '@#$%^876$%^&*OIUYTRTYUIJHG^&*((*&^$%^&*'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:25251025@localhost/labphongmachdb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
flask_change_password = ChangePassword(min_password_length=10, rules=dict(long_password_override=2))
flask_change_password.init_app(app)

db = SQLAlchemy(app=app)

babel = Babel(app=app)


@babel.localeselector
def get_locale():
        return 'vi'


login = LoginManager(app=app)