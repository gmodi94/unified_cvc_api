from main import app
import json
import traceback
import redis

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


# async def add_transcations(to_id,from_id):
# 	try:

# 		redis_con.hmset("Transactions_details:"+t_id,"from",from_id,"to",to_id)