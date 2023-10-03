from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



db = SQLAlchemy()


app = Flask(__name__)
#Forms:
app.config[
    "SECRET_KEY"
] = "62913a7dac3933f87a84626fcdeaaf9e2653f0a000843efd9bf2b31ba4767402"
#DATABASE:
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///first.db'
db.init_app(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True



bcrypt = Bcrypt(app)




login_manager = LoginManager(app)
from routes import main_bp
app.register_blueprint(main_bp)
login_manager.login_view = "main.login"
login_manager.login_message_category = "info"    



@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))






if __name__ == "__main__":
    
    from routes import main_bp
    
    login_manager.init_app(app)
    app.run(debug=True)
