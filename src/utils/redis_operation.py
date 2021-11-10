from utils.helper import qr
from main import app
from models import db
import json
import traceback
import redis
from models.Transcationmodel import transcation_details
from models.userdetails import UserDetails
import jwt

redis_con = redis.Redis(host="localhost",
                        port=6379,
                        db=5,
                        decode_responses=True)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

async def check_user_details(user):
	try:
		user_details = redis_con.hget("USER_DETAILS",user)
		if user_details:
			user_details = json.loads(user_details)
			if user_details.get("active") != 1:
				raise Exception("eror")
				return True, {}
		else:
			raise Exception("eror")
			return True, {}
	except Exception:
		traceback.print_exc()
		raise Exception("eror")
		return True, {}
	return False, user_details


async def add_transcations(to_id,from_id):
	t1 = transcation_details(from_id=from_id,to_id=to_id,status="pending")
	db.session.add(t1)
	db.session.commit()
	t_id = t1.id
	print(t_id)
	redis_con.hmset("Transactions_details:"+str(t_id),{"from":from_id,"to":to_id})
	redis_con.expire("Transactions_details:"+str(t_id), 3600)
	return t_id


async def add_user(data):
	db.create_all()
	insert_data = {
            "first_name" : data["first_name"],
            "last_name" : data["last_name"],
            "mobile_number": data["mobile_number"],
            "extra_notes": data["extra_notes"],
            "address": data["address"],
        }
	user_id = UserDetails(**insert_data)
	print(user_id.last_name)
	db.session.add(user_id)
	db.session.commit()
	encoded_jwt = jwt.encode({"user_id": str(user_id.id)}, "secret", algorithm="HS256")
	insert_data["jwt_tokens"] = encoded_jwt
	user_id.jwt_tokens = encoded_jwt
	redis_con.hmset("user_details:"+str(user_id.mobile_number),insert_data)
	db.session.add(user_id)
	db.session.commit()
	blob_data =	qr(str(user_id.id),data["first_name"],data["last_name"])
	user_id.blob_file = blob_data
	db.session.commit()

async def add_otp(data,d):
		redis_con.hset(f"OTP_DETAILS:{d['mobile_number']}", "Data", json.dumps(data))
		redis_con.expire(f"OTP_DETAILS:{d['mobile_number']}", 120)

async def validate_otp(mobile_number):
	data = redis_con.hget(f"OTP_DETAILS:{mobile_number}", "Data")
	print(data)
	return data
async def delete_otp(mobile_number):
    redis_con.delete(f"OTP_DETAILS:{mobile_number}")

async def get_token(mobile_number):
	token = redis_con.hget("user_details:"+str(mobile_number),"jwt_tokens")
	return token

async def get_user_details(id):
	user = UserDetails.query.filter_by(id=id).first()
	print(user)
	return user