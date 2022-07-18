import os
from functools import wraps

import jwt
from flask import request, jsonify, session
from src.common.response import Response,ResponseCodes,ResponseMessage
from src.models.user import User
import sys


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return Response.error(code=ResponseCodes.not_found.value,message=ResponseMessage.token_missing_message.value,status='token not found')
        try:
            data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
            # kwargs['current_user'] = current_user
        except:
            return Response.error(ResponseCodes.un_authorized.value,message=ResponseMessage.invalid_token_message.value,
                                  status="un authorized")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)
        return f(current_user,*args,**kwargs)

    return decorator

def current_user_login():
    if 'x-access-tokens' in request.headers:
        token = request.headers['x-access-tokens']

    if not token:
        return Response.error(code=ResponseCodes.not_found.value, message=ResponseMessage.token_missing_message.value,
                          status='token not found')
    data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
    current_user = User.query.filter_by(public_id=data['public_id']).first()
    return current_user
