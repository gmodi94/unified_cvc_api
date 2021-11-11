from main import app
from flask import request,jsonify
from utils.redis_operation import add_otp, add_transcations, add_user,delete_otp,get_token, get_user_details,validate_otp,fetch_details
from utils.message_sender import send_message
from config import MESSAGE_PAYLOAD,RICH_TEXT_PAYLOAD,FALLBACK_PAYLOAD
from utils.decorators import middleware
from models import db
from datetime import timedelta,datetime

# from models.userdetails import UserDetails
import traceback
import jwt
import random
# import datetime
import json


@app.route('/v1/send_otp', methods = ['POST'])
async def send_otp():
    try:
        db.create_all()
        d = request.json
        otp = random.randint(1000,9999)
        message = f"Your OTP is {otp}"
        expiry_time = (datetime.now() + timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")
        data = {
        "otp":otp,
        "expiry_time":expiry_time}
        await add_otp(data,d)
        send_message(message,"sms",phonenumber=d["mobile_number"])
        return {"status":"success"}
    except :
        traceback.print_exc()
        return {"status":"failure"}

@app.route('/v1/validate_otp', methods = ['POST'])
async def validate():
    try:
        d = request.json

        mobile_number = d["mobile_number"]
        data = await validate_otp(mobile_number)
        data = json.loads(data)
        expiry_time = datetime.strptime(data["expiry_time"], "%Y-%m-%d %H:%M:%S")
        print(expiry_time,expiry_time > datetime.now(),datetime.now())
        if expiry_time > datetime.now():
            if str(data["otp"]) == d["otp"]:
                await delete_otp(mobile_number)
                if d["action"]=="sign_up":
                    return {"status":"success"}
                elif d['action'] == "log_in":
                    token = await get_token(mobile_number)
                    return {"status":"success","token":token}
            else:
                return {"status":"invalid"}
        else:
            return {"status":"expired"}
    except:
        traceback.print_exc()
        return {"status":"expired"}


@app.route("/v1/scan",methods=["post"])
@middleware
async def scan(from_id):
    payload = request.get_json()
    print(from_id)
    if payload.get("id","")=="":
        return jsonify({"status":False})
    to_id = payload["id"]
    t_id = await add_transcations(to_id,from_id)
    sender = await get_user_details(from_id)
    user = await get_user_details(to_id)
    number = user.mobile_number
    name = user.first_name
    sendername = sender.first_name
    payload = MESSAGE_PAYLOAD
    payload["phone"] = number
    payload["media"]["body"] = payload["media"]["body"].format(name,sendername)
    payload["media"]["button"][0]["id"] = "yes:"+str(t_id)
    payload["media"]["button"][1]["id"] = "no:"+str(t_id)
    print(payload)
    send_message(payload,"wbm")
    return jsonify({"status":True})



@app.route("/v1/callback",methods=["post"])
async def callback():
    try:
        callback_payload = request.get_json()
        # print("callback_payload",callback_payload)
        user_contact = callback_payload['user_contact']

        #If yes to connect
        answer = callback_payload['messages'][0]['interactive']['button_reply']['title']
        transaction_id = callback_payload['messages'][0]['interactive']['button_reply']['id'].split(":")[1]
        users = await fetch_details(transaction_id)
        for user in users:
            print(user)
            user_details = await get_user_details(user)
            if answer == "Yes":
                final_payload = RICH_TEXT_PAYLOAD 
                full_name = user_details.first_name + user_details.last_name
                final_payload["phone"] = user_details.mobile_number
                final_payload["media"]["caption"] = final_payload["media"]["caption"].format(user_details.first_name,full_name,user_details.mobile_number,user_details.address,user_details.extra_notes)
                print(final_payload)
            else:
                final_payload = FALLBACK_PAYLOAD
                final_payload["phone"] = user_details.mobile_number
                final_payload["text"] = "Successfully Rejected" if user == users[1] else "Your request has deined by the user"

            send_message(final_payload,"wbm")
        #fetch the registeration details based on the transaction details ka id and return the final payload to be sent
        #from_id to_id ka two payloads banana hain matlab?? need to ask gaurav
        # from_id,to_id,f_name,l_name,phn_num,address = fetch_details(user_contact,transaction_id)
        #creation of final_payload
    # If No
        # if callback_payload['messages'][0]['interactive']['button_reply']['title'] == "Yes":
        #     pass
        # else:

        #     send_message(final_payload,"wbm")
        #send payload via whatsapp channel

    except Exception as e:
        traceback.print_exc()
    return {"status": "ok"}


@app.route('/v1/registration',methods = ['POST'])
async def registration():
    try:
        data = request.json
        # data= ValidateData().load(data)
        await add_user(data)
        return {"status":"success"}
    except Exception as e:
        traceback.print_exc()
        return {"status": "failed", "errors": "Contact administration for more info"},500

if "__main__" == __name__:
    db.create_all()
    app.run()
