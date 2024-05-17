import jwt
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

load_dotenv()
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'this is a secret'
jwt = JWTManager(app)

# Storing users in a list of dictionaries
users = []

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/users/", methods=["POST"])
def add_user():
    try:
        user_data = request.json
        if not user_data:
            return jsonify({
                "message": "Please provide user details",
                "error": "Bad request"
            }), 400

        # Check if the user already exists
        for user in users:
            if user['email'] == user_data['email']:
                return jsonify({
                    "message": "User already exists",
                    "error": "Conflict"
                }), 409

        users.append(user_data)
        return jsonify({
            "message": "Successfully created new user",
            "data": user_data
        }), 201
    except Exception as e:
        return jsonify({
            "message": "Something went wrong",
            "error": str(e)
        }), 500

@app.route("/users/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({
                "message": "Please provide user details",
                "error": "Bad request"
            }), 400

        # Find user in the list by email and password
        for user in users:
            if user['email'] == data.get('email') and user['password'] == data.get('password'):
                try:
                    # Generate access token
                    access_token = create_access_token(identity=user['email'])
                    return jsonify({
                        "message": "Successfully fetched auth token",
                        "data": {"token": access_token}
                    })
                except Exception as e:
                    return jsonify({
                        "error": "Something went wrong",
                        "message": str(e)
                    }), 500

        return jsonify({
            "message": "Error fetching auth token! Invalid email or password",
            "error": "Unauthorized"
        }), 404
    except Exception as e:
        return jsonify({
            "message": "Something went wrong!",
            "error": str(e)
        }), 500

@app.route("/users/", methods=["GET"])
@jwt_required()  # Protected route
def get_users():
    return jsonify({
        "message": "Successfully retrieved users",
        "data": users
    })

@app.errorhandler(403)
def forbidden(e):
    return jsonify({
        "message": "Forbidden",
        "error": str(e)
    }), 403

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "message": "Endpoint Not Found",
        "error": str(e)
    }), 404

if __name__ == "__main__":
    app.run(debug=True)
