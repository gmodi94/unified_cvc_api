import re

from sqlalchemy.orm import load_only
from src.models.otpdetails import otp_details
from src.utils.helper import csv_to_base64, qr, user_to_vcard
from src.main import app
from src.models import db
import json
import traceback
import redis
from src.models.Transcationmodel import transcation_details
from src.models.userdetails import UserDetails
import jwt
try:
	redis_con = redis.Redis(host="localhost",
							port=6379,
							db=5,
							decode_responses=True)
except:
	redis_con = redis.Redis()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

async def fetch_details(transaction_id):
	try:
		transaction_records =redis_con.hmget("Transactions_details:"+str(transaction_id),"from","to")
		# print(transaction_records)
		if transaction_records is not None:
			from_id = transaction_records[0]
			to_id = transaction_records[1]
			print("from_id",from_id,"to_id",to_id)
			return transaction_records
	except:
		transaction_records = transcation_details.query.filter_by(id=transaction_id).first()
		if transaction_records.status == "Complete":
			return "True"
		transaction_records = [transaction_records.from_id,transaction_records.to_id]
		return transaction_records

async def up_transaction(transaction_id,status):
	transaction_records = transcation_details.query.filter_by(id=transaction_id).first()
	transaction_records.status = status
	db.session.commit()


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
	try:
		redis_con.hmset("Transactions_details:"+str(t_id),{"from":from_id,"to":to_id})
		redis_con.expire("Transactions_details:"+str(t_id), 3600)
	except:
		pass
	return t_id


async def add_user(data):
	db.create_all()
	u = UserDetails.query.filter_by(mobile_number=data["mobile_number"]).first()
	if u:
		return False
	insert_data = {
            "first_name" : data["first_name"],
            "last_name" : data["last_name"],
            "mobile_number": data["mobile_number"],
            "extra_notes": data["extra_notes"],
            "address": data["address"],
			"email":data["email"]
        }
	user_id = UserDetails(**insert_data)
	print(user_id.last_name)
	db.session.add(user_id)
	db.session.commit()
	encoded_jwt = jwt.encode({"user_id": str(user_id.id)}, "secret", algorithm="HS256")
	insert_data["jwt_tokens"] = encoded_jwt
	user_id.jwt_tokens = encoded_jwt
	try:
		redis_con.hmset("user_details:"+str(user_id.mobile_number),insert_data)
	except:
		pass
	db.session.add(user_id)
	db.session.commit()
	blob_data =	qr(str(user_id.id),data["first_name"],data["last_name"])
	user_id.blob_file = str(blob_data)
	db.session.commit()
	return True

async def add_otp(data,d):
	try:
		redis_con.hset(f"OTP_DETAILS:{d['mobile_number']}", "Data", json.dumps(data))
		redis_con.expire(f"OTP_DETAILS:{d['mobile_number']}", 120)
		otpdata = otp_details.query.filter_by(mobile_number=d['mobile_number']).first()
		if otpdata is not None:
			otpdata.otp_data = json.dumps(data)
			db.session.add(otpdata)
		else:
			otp = otp_details(otp_data=json.dumps(data),mobile_number=d["mobile_number"])
			db.session.add(otp)
		db.session.commit()
	except:
		otpdata = otp_details.query.filter_by(mobile_number=d['mobile_number']).first()
		if otpdata is not None:
			otpdata.otp_data = json.dumps(data)
			db.session.add(otpdata)
		else:
			otp = otp_details(otp_data=json.dumps(data),mobile_number=d["mobile_number"])
			db.session.add(otp)
		db.session.commit()
		

async def validate_otp(mobile_number):
	try:
		data = redis_con.hget(f"OTP_DETAILS:{mobile_number}", "Data")
		print(data)
	except:
		otp_data = otp_details.query.filter_by(mobile_number=mobile_number).first()
		data = otp_data.otp_data
		print(type(data))
	return data
async def delete_otp(mobile_number):
	try:
		redis_con.delete(f"OTP_DETAILS:{mobile_number}")
		otp_details.query.filter_by(mobile_number=mobile_number).delete()
		db.session.commit()
	except:
		otp_details.query.filter_by(mobile_number=mobile_number).delete()
		db.session.commit()	


async def get_token(mobile_number):
	u = UserDetails.query.filter_by(mobile_number=mobile_number).first()
	try:
		token = redis_con.hget("user_details:"+str(mobile_number),"jwt_tokens")
	except:
		token = u.jwt_tokens
	blob = u.blob_file
	return token,blob

async def get_user_details(id):
	user = UserDetails.query.filter_by(id=id).first()
	print(user)
	return user

async def get_user_details_from_number(mobile_number):
	user = UserDetails.query.filter_by(mobile_number=mobile_number).first()
	print(user)
	return user

async def check_ban(from_id,to_id=""):
	u = transcation_details.query.filter(transcation_details.from_id==from_id).options(load_only("status")).all()
	lisoft = [i.to_id for i in u if i.status == "ban"]
	banlen = len(lisoft)
	print(lisoft)
	if banlen > 2:
		return True
	if to_id in lisoft:
		return True
	print(banlen)
	return False
	


async def get_list(id):
	u = transcation_details.query.filter(transcation_details.from_id==id,transcation_details.status=="Complete").options(load_only("to_id")).all()
	listofusers = list(set([i.to_id for i in u ]))
	print(listofusers)
	return listofusers

async def get_csv_vcard(users):
	users = UserDetails.query.filter(UserDetails.id.in_(users)).all()
	heads = ["first_name","last_name","email","notes","address"]
	csvdata = [[user.first_name,user.last_name,user.email,user.extra_notes,user.address]for user in users]
	csvdata.insert(0,heads)
	vcardlist = [user_to_vcard(user) for user in users]
	print(vcardlist)
	vcardlist.append({
                "type": "text/plain",
                "name": "mycontact.csv",
                "content": csv_to_base64(csvdata).decode()
            })
	return vcardlist

	