from redis import connection
from src.main import app
from flask import request,jsonify,redirect
from src.utils.redis_operation import *
from src.utils.message_sender import capability, send_message
from src.config import *
from src.utils.decorators import middleware
from src.models import db
from datetime import timedelta,datetime
import requests
import mimetypes

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
        if not capability(d['mobile_number']):
            return {"status":"Invalid Whatsapp number"}
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
                if d["action"]=="sign_up":
                    return {"status":"success",}
                elif d['action'] == "log_in":
                    token, blob = await get_token(mobile_number)
                    print(blob)
                    return {"status":"success","token":token,"qrimage":str(blob)}
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
    user = await get_user_details(to_id)
    if user is None:
        return {"status":"user does not exist"}
    if to_id == from_id:
        return {"status":"Same User"}
    if await check_ban(from_id,to_id):
        return {"status":"You are been ban"}

    t_id = await add_transcations(to_id,from_id)
    sender = await get_user_details(from_id)
    user = await get_user_details(to_id)
    if user is None:
        return {"status":"user does not exist"}
    number = user.mobile_number
    name = user.first_name
    sendername = sender.first_name
    payload = MESSAGE_PAYLOAD
    payload["phone"] = number
    payload["media"]["body"] = payload["media"]["body"].format(name,sendername)
    payload["media"]["button"][0]["id"] = "yes:"+str(t_id)
    payload["media"]["button"][1]["id"] = "no:"+str(t_id)
    payload["media"]["button"][2]["id"] = "Spam:"+str(t_id)
    print(payload)
    send_message(payload,"wbm")
    return jsonify({"status":True})



@app.route("/v1/callback",methods=["post"])
async def callback():
    try:
        callback_payload = request.get_json()
        # print("callback_payload",callback_payload)
        # user_contact = callback_payload['user_contact']
        #If yes to connect
        if'interactive' in callback_payload["messages"][0].keys():
            answer = callback_payload['messages'][0]['interactive']['button_reply']['title']
            transaction_id = callback_payload['messages'][0]['interactive']['button_reply']['id'].split(":")[1]
            users = await fetch_details(transaction_id)
            print(users)
            if users == "True" :
                return {"status":"ok"}
            user_details1 = await get_user_details(users[0])
            user_details2 = await get_user_details(users[1])
            users = [user_details1,user_details2]
                
            if answer == "Yes":
                final_payload = RICH_TEXT_PAYLOAD 
                full_name = user_details2.first_name +" "+ user_details2.last_name
                final_payload["phone"] = user_details1.mobile_number
                final_payload["media"]["caption"] = "Contact Details Received From {}: \n \n*Name:* {} \n \n*Mobile Number:* {} \n \n*Email:* {}  \n \n*Address:* {}  \n \n*Notes:* {}".format(user_details2.first_name,full_name,user_details2.mobile_number,user_details2.email,user_details2.address,user_details2.extra_notes)
                print(final_payload)
                send_message(final_payload,"wbm")
                # final_payload = RICH_TEXT_PAYLOAD 
                full_name = user_details1.first_name + user_details1.last_name
                final_payload["phone"] = user_details2.mobile_number
                final_payload["media"]["caption"] = "Contact Details Received From {}: \n \n*Name:* {} \n \n*Mobile Number:* {} \n \n*Email:* {}  \n \n*Address:* {}  \n \n*Notes:* {}".format(user_details1.first_name,full_name,user_details1.mobile_number,user_details1.email,user_details1.address,user_details1.extra_notes)
                print(final_payload)
                send_message(final_payload,"wbm")

                rcspayload = RCS_PAYLOAD
                full_name = user_details1.first_name +" "+ user_details1.last_name
                rcspayload['phone_no'] = user_details2.mobile_number
                rcspayload['card']['title'] = "Bussiness Card of "+full_name
                rcspayload['card']['suggestions'][0]['text'] = "Whatsapp "+user_details1.first_name
                rcspayload['card']['suggestions'][1]['text'] = "Mail "+user_details1.first_name
                rcspayload['card']['suggestions'][2]['text'] = "Call "+user_details1.first_name
                rcspayload['card']['suggestions'][0]['url'] = "http://wa.me/"+user_details1.mobile_number
                rcspayload['card']['suggestions'][1]['url'] = "https://conviscard.herokuapp.com/mail?mail="+user_details1.email
                rcspayload['card']['suggestions'][2]['call_to'] = user_details1.mobile_number

                send_message(rcspayload,"rcs")

                full_name = user_details2.first_name +" "+ user_details2.last_name
                rcspayload['phone_no'] = user_details1.mobile_number
                rcspayload['card']['title'] = "Bussiness Card of "+full_name
                rcspayload['card']['suggestions'][0]['text'] = "Whatsapp "+user_details2.first_name
                rcspayload['card']['suggestions'][1]['text'] = "Mail "+user_details2.first_name
                rcspayload['card']['suggestions'][2]['text'] = "Call "+user_details2.first_name
                rcspayload['card']['suggestions'][0]['url'] = "http://wa.me/"+user_details2.mobile_number
                rcspayload['card']['suggestions'][1]['url'] = "https://conviscard.herokuapp.com/mail?mail="+user_details2.email
                rcspayload['card']['suggestions'][2]['call_to'] = user_details2.mobile_number

                send_message(rcspayload,"rcs")
                await up_transaction(transaction_id,"Complete")



            elif answer == "No":
                final_payload = FALLBACK_PAYLOAD
                final_payload["phone"] = user_details1.mobile_number
                final_payload["text"] = "Your request has deined by {}".format(user_details2.first_name)
                send_message(final_payload,"wbm")
                final_payload["phone"] = user_details2.mobile_number
                final_payload["text"] = "Rejection Successfull"
                send_message(final_payload,"wbm")
                await up_transaction(transaction_id,"Failed")

            elif answer == "Spam":
                await up_transaction(transaction_id,"ban")
        elif "text" in callback_payload["messages"][0].keys():
            if callback_payload["messages"][0]["text"]["body"].lower() == "my contacts":
                number = callback_payload["messages"][0]["from"]
                user = await get_user_details_from_number("+"+number)
                users = await get_list(str(user.id))
                if users == []:
                    connection = False
                else :
                    connection = True
                if connection == True:
                    vcardlist = await get_csv_vcard(users)
                    final_payload = MAIL_PAYLOAD
                    # final_payload["message"]["attachments"][0]["content"]=csvbase.decode()
                    final_payload["message"]["attachments"].extend(vcardlist)
                    final_payload["message"]["to"][0]["email"]=user.email
                    final_payload["message"]["to"][0]["name"]=user.first_name+" "+user.last_name
                    print(final_payload)
                    send_message(final_payload,"mail")
                    payload = SIMPLEPAYLOAD
                    payload["phone"] = "+"+number
                    payload["text"] = "we have mailed your list on your email id "+user.email
                    send_message(payload,"wbm")
                else:
                    payload = SIMPLEPAYLOAD
                    payload["phone"] = "+"+number
                    payload["text"] = "You have no connection till Now"
                    send_message(payload,"wbm")
            else:
                number = callback_payload["messages"][0]["from"]
                payload = SIMPLEPAYLOAD
                payload["phone"] = "+"+number
                payload["text"] = "Hi Welcome to CVC , \nIf You wish to get all your connection Please type \"my contacts\""
                send_message(payload,"wbm")






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
        return {"status":"ok"}
    except Exception as e:
        traceback.print_exc()
    return {"status": "ok"}


@app.route('/v1/registration',methods=['POST'])
async def registration():
    try:
        data = request.json
        # data= ValidateData().load(data)
        if not await add_user(data):
            return {"status": "User Exist"}
        await add_user(data)
        payload = "Registration is successful \n Please click on this link and send the \"Hi\" message \n https://wa.me/+918928894215?text=Hi"
        send_message(payload,"sms",data["mobile_number"])
        return {"status":"success"}
    except Exception as e:
        traceback.print_exc()
        return {"status": "failed", "errors": "Contact administration for more info"},500

@app.route("/v1/bulksend",methods=['POST'])
@middleware
async def send_bulk(from_id):
    try:
        if await check_ban(from_id):
            return {"status":"You are been ban"}
        from_user = await get_user_details(from_id)
        url = request.get_json().get("url")
        channel = request.get_json().get("channel","")
        response = requests.get(url)
        content_type = response.headers['content-type']
        extension = mimetypes.guess_extension(content_type)
        if extension not in [".png",".jpg",".jpeg"]:
            print(extension)
            return {"error":"only img file"}
        users = await get_list(from_id)
        if users == []:
            return {"status":"You have no connection till now"}
        for user in users:
            user = await get_user_details(user)
            if not await check_ban(from_id,str(user.id)):
                if channel == "Whatsapp":
                    payload = BULKPAYLOAD
                    payload['phone'] = user.mobile_number
                    payload["media"]["url"] = url
                    payload["media"]["caption"] = "Message From "+from_user.first_name 
                    payload["media"]["caption"] = "Message From "+from_user.first_name 
                    send_message(payload,"wbm")
                elif channel == "RCS":
                    payload = RCS_BULK_PAYLOAD
                    payload["phone_no"] = user.mobile_number  
                    payload["card"]["title"] = "Message From "+from_user.first_name
                    payload["card"]["url"] = url
                    send_message(payload,"rcs")
                elif channel == "mail":
                    final_payload = BULK_MAIL_PAYLOAD
                    final_payload["message"]["html"] = "<img src="+url+" width='500' height='500'>" 
                    final_payload["message"]["to"][0]["email"]=user.email
                    final_payload["message"]["to"][0]["name"]=user.first_name+" "+user.last_name
                    final_payload["message"]["text"] = "Message From "+from_user.first_name
                    final_payload["message"]["from_name"] = from_user.first_name+" "+from_user.last_name
                    print(final_payload)
                    send_message(final_payload,"mail")
                else:
                    payload = BULKPAYLOAD
                    payload['phone'] = user.mobile_number
                    payload["media"]["url"] = url
                    payload["media"]["caption"] = "Message From "+from_user.first_name 
                    send_message(payload,"wbm")
                    payload = RCS_BULK_PAYLOAD
                    payload["phone_no"] = user.mobile_number  
                    payload["card"]["title"] = "Message From "+from_user.first_name
                    payload["card"]["url"] = url
                    send_message(payload,"rcs")
                    final_payload = BULK_MAIL_PAYLOAD
                    final_payload["message"]["html"] = "<img src="+url+" width='500' height='500'>"  
                    final_payload["message"]["text"] = "Message From "+from_user.first_name
                    final_payload["message"]["to"][0]["name"]=user.first_name+" "+user.last_name
                    final_payload["message"]["from_name"] = from_user.first_name+" "+from_user.last_name
                    final_payload["message"]["to"][0]["email"]=user.email
                    print(final_payload)
                    send_message(final_payload,"mail")

        return {"status":"success"}
    except Exception as e:
        return{"url":"invalid "+str(e)}
    
    





@app.route('/mail')
def mail():
    user = request.args.get('mail')
    return redirect('mailto:{}'.format(user))




if "__main__" == __name__:
    db.create_all()
    app.run()
