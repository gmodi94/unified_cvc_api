import jwt
import traceback
import json
from flask import jsonify,request       

from functools import wraps

from utils.redis_operation import check_user_details
# from utils.redis_operations import check_user_details, check_merchant_details

def middleware(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            auth_token = request.headers.get('authorization')
            token_details = jwt.decode(
                auth_token, 'secret', algorithms=['HS256'])
            # print(token_details)
            user_id= token_details["user_id"]
            await check_user_details(user_id)
            # return "hello"
            return await func(user_id)
        except json.decoder.JSONDecodeError:
            traceback.print_exc()
            return "error"  
        except Exception as e:
            traceback.print_exc()
            return "error"
    return wrapper