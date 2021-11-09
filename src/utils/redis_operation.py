from main import app
import json
import traceback
import redis

redis_con = redis.Redis(host="localhost",
                        port=6379,
                        db=5,
                        decode_responses=True)

async def check_user_details(user):
	try:
		user_details = await redis_con.hget("USER_DETAILS",user)
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
