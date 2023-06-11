from main.Database import Database
from user.UserModel import UserModel
from flask import current_app, jsonify
from flask_login import login_user, logout_user
import datetime


class UserHandler:
    def __init__(self):
        self.db = Database(current_app)
        self.collection_name = 'users'

    def signup(self, r_data):
        email = r_data.get('email')
        password = r_data.get('password')
        username = r_data.get('username')
        is_admin = r_data.get('is_admin')
        print(email, password, username, is_admin)
        user = UserModel(email, password, username, is_admin)

        duplicate_user = self.db.find_one(self.collection_name, {'email': email})
        if duplicate_user:
            return jsonify({'status': 'fail', 'message': 'User already exists.'})
        else:
            new_user = {
                "email": user.email,
                "password": user.password_hash,
                "username": user.username,
                "is_admin": user.is_admin,
            }
            self.db.insert(self.collection_name, new_user)
            return jsonify({'status': 'success', 'message': 'User created.'})

    def login(self, r_data):
        email = r_data.get('email')
        password = r_data.get('password')
        user_data = self.db.find_one(self.collection_name, {'email': email})
        user = UserModel(
            user_data.get('email'),
            user_data.get('password'),
            user_data.get('username'),
            user_data.get('is_admin'),
        )
        user.id = user_data.get('_id')

        if user_data:
            if user.check_password(password):
                login_user(user)
                return jsonify({'status': 'success', 'message': 'Login success'})
            else:
                return jsonify(
                    {
                        'status': 'fail',
                        'message': 'User account or user password is wrong.',
                    }
                )
        else:
            return jsonify(
                {
                    'status': 'fail',
                    'message': 'User account or user password is wrong.',
                }
            )
