import os
import uuid
from datetime import datetime, timedelta

import jwt
from flask import request, make_response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from src import api_test, app
from src.models import db
from src.models.user import User
from src.common.response import Response, ResponseCodes, ResponseMessage
from src.common.helper import ProjectHelper



@api_test.route("/add_user", methods=["POST"])
def add_user():
    try:
        email = request.form.get("email", None)
        user_name = request.form.get("username")
        first_name = request.form.get("first_name", " ")
        last_name = request.form.get("last_name", " ")
        is_superuser = bool(request.form.get("is_superuser", False))
        is_active = bool(request.form.get("is_active", True))
        is_admin = bool(request.form.get("is_admin", False))
        password = request.form.get("password", "pass@1234")
        hash_password = generate_password_hash(password, method='sha256')
        public_id = str(uuid.uuid4())
        if len(password) < 9:
            raise ValueError("failed password  validation")

        if email:
            user_object = User(email=email,
                               username=user_name,
                               first_name=first_name,
                               last_name=last_name,
                               password=hash_password,
                               public_id=public_id,
                               is_superuser=is_superuser,
                               is_active=is_active,
                               is_admin=is_admin)

            User.save(user_object)
            response = Response.success(message=ResponseMessage.get_success_message.value,
                                        code=ResponseCodes.success.value, data=[])
        else:
            response = Response.error(message=ResponseMessage.precondition_failed_message.value,
                                      code=ResponseCodes.precondition_failed.value)

    except Exception as e:
        response = Response.error(message=ResponseMessage.exception_message.value + str(e))
    return response


@api_test.route("/update_user", methods=["PUT"])
def update_user():
    try:
        user_object = {
            'id': request.form.get("user_id",0),
            "is_superuser": bool(request.form.get("is_superuser", False)),
            "is_admin": bool(request.form.get("is_admin", False)),
            "is_active": bool(request.form.get("is_active", False)),
        }
        user = User.update_user(user_object.get('user_id'), user_object)
        response = Response.success(message=ResponseMessage.get_success_message.value, code=ResponseCodes.success.value,
                                    data=[])
    except Exception as e:
        response = Response.error(message=ResponseMessage.exception_message.value + str(e))
    return response


@api_test.route('/login', methods=['POST'])
def login_user():
    """
    It works also with swag_from, schemas and spec_dict
    ---
    parameters:
      - in: auth
        name: username
        type: string
        required: false
      - in : path
        name: password
        type: string
        required: false
    responses:
      200:
        description: A single user item
        schema:
          id: User
          properties:
            username:
              type: string
              description: The name of the user
              default: Steven Wilson
        """
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'Authentication': 'login required"'})

    user = User.query.filter_by(username=auth.username).first()
    if check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {'public_id': user.public_id, 'exp': datetime.utcnow() + timedelta(minutes=45)},
            os.environ.get('SECRET_KEY',''), "HS256")
        return jsonify({
            'x-access-tokens': token,
            # "user": {
            #     "id": user.id,
            #     "email": user.username,
            #     "first_name": user.first_name,
            #     "last_name": user.last_name
            # }
        })

    return make_response('could not verify', 401, {'Authentication': '"login required"'})
