from functools import wraps

import jwt
from flask import request, jsonify

TOKEN_HEADER = 'x-access-token'

def required_admin(f):
    # wrap the function name to avoid
    # AssertionError: View function mapping is overwriting an existing endpoint function
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        # jwt is passed in the request header
        if TOKEN_HEADER in request.headers:
            token = request.headers[TOKEN_HEADER]
        else:
            # return 401 if token is not passed
            return jsonify({'message': 'Token is missing'}), 401

        try:
            # decoding the token
            decoded_jwt = jwt.decode(token, options={"verify_signature": False})
            roles_jwt = decoded_jwt.get('roles')
            # check if the roles in jwt allowed is admin
            if 'admin' in roles_jwt:
                return f(*args, **kwargs)
            else:
                # return 403 if the role is not allowed
                return jsonify({
                    'message': 'Not authorized to access the API'
                }), 403
        except Exception as e:
            return jsonify({
                'message': 'Token is invalid',
                'error': str(e)
            }), 403

    return wrapped_f

def required_viewer(f):
    # wrap the function name to avoid
    # AssertionError: View function mapping is overwriting an existing endpoint function
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        # jwt is passed in the request header
        if TOKEN_HEADER in request.headers:
            token = request.headers[TOKEN_HEADER]
        else:
            # return 401 if token is not passed
            return jsonify({'message': 'Token is missing'}), 401

        try:
            # decoding the token
            decoded_jwt = jwt.decode(token, options={"verify_signature": False})
            roles_jwt = decoded_jwt.get('roles')
            # check if the roles in jwt allowed is admin or viewer
            if 'admin' in roles_jwt or 'viewer' in roles_jwt:
                return f(*args, **kwargs)
            else:
                # return 403 if the role is not allowed
                return jsonify({
                    'message': 'Not authorized to access the API'
                }), 403
        except Exception as e:
            return jsonify({
                'message': 'Token is invalid',
                'error': str(e)
            }), 403

    return wrapped_f
    