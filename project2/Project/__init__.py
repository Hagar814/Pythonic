from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager





app = Flask(__name__)
#Forms:
app.config[
    "SECRET_KEY"
] = "62913a7dac3933f87a84626fcdeaaf9e2653f0a000843efd9bf2b31ba4767402"
#DATABASE:
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///first.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"



    
 


from Project.routes import main_bp
app.register_blueprint(main_bp)

