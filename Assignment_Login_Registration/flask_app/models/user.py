from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import bcrypt
from datetime import date, datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.username = data['username']
        self.password = data['password']
        self.birthday = data['birthday']
        self.pro_lang = data['pro_lang']
        self.cat_dog = data['cat_dog']
        self.seasons = data['seasons']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, username, password, birthday, pro_lang, cat_dog, seasons, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(username)s,%(password)s,%(birthday)s,%(pro_lang)s,%(cat_dog)s,%(seasons)s,NOW(),NOW());"
        result = connectToMySQL('mydb').query_db(query,data)
        return result
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        return cls(result[0])
    
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 2:
            flash("First Name must be at least 2 characters.", "register")
            is_valid = False
        if not user['first_name'].isalpha():
            flash("First Name must only be letters", "register")
            is_valid = False
            
        if len(user['last_name']) < 2:
            flash("Last Name must be at least 2 characters.", "register")
            is_valid = False
        if not user['last_name'].isalpha():
            flash("Last Name must only be letters", "register")
            is_valid = False
            
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,user)
        if len(result) >= 1: 
            flash("Email Already Taken", "register")
            is_valid = False
        
        query = "SELECT * FROM users WHERE username = %(username)s;"
        result = connectToMySQL("mydb").query_db(query,user)
        if len(result) >= 1:
            flash("Username Already Taken", "register")
            is_valid = False
            
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.", "register")
            is_valid = False
        if user['password'].isalpha():
            flash("Password must have at least 1 number", "register")
            is_valid = False
        if user['password'].islower():
            flash("Password must have at least 1 uppercase letter", "register")
            is_valid = False
        if user['password'] != user['password_2']:
            flash("Passwords don't match", "register")
            is_valid = False
            
        if user['birthday'] == "":
            flash("You must enter a date", "register")
            is_valid = False
        if (date.today().year - datetime.strptime(user['birthday'], '%Y-%m-%d').year) < 10:
            flash("You must be at least 10 years old", "register")
            is_valid = False
            
        if user['cat_dog'] != 'cat' and user['cat_dog'] != 'dog':
            flash("Must select cat or dog", "register")
            is_valid = False
            
        if user['seasons'] != 'Fall' and user['seasons'] != 'Winter' and user['seasons'] != 'Spring' and user['seasons'] != 'Summer':
            flash("Must select at least one season", "register")
            is_valid = False
        return is_valid