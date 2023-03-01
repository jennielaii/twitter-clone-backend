# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config["SQALCHEMY_DATABASE_URI"] = "sqlite:///twitter.db"

# # Database 
# db = SQLAlchemy(app)
# class Users(db.Model):
#     id = db.Column('student_id', db.Integer, primary_key = True) 
#     username = db.Column(db.String(24))
#     email = db.Colum(db.String(64))
#     pwd = db.Column(db.String(64))

#     # Constructor
#     def __init__(self, username, email, pwd):
#         self.username = username
#         self.email = email
#         self.pwd = pwd

# @app.route('/')
# def index():
#     return "Hello, world!"

# if __name__ == "__main__":
#     app.run(debug=True) # debug=True restarts the server everytime we make a change in our code

