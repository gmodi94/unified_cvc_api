from main import app
from flask import request,jsonify
# from utils.redis_operation import add_transcations
from utils.message_sender import send_message
from config import MESSAGE_PAYLOAD
from utils.decorators import middleware





@app.route("/v1/scan",methods=["post"])
@middleware
async def scan(from_id):
    payload = request.get_json()
    print(from_id)
    if payload.get("id","")=="":
        return jsonify({"status":False})
    to_id = payload["id"] 
    # add_transcations(to_id,from_id)
    number = "+919769187972"
    name = "Gaurav"
    payload = MESSAGE_PAYLOAD
    payload["phone"] = number
    payload["media"]["body"] = payload["media"]["body"].format(name)
    send_message(payload)
    return jsonify({"status":True})
    

@app.route("/v1/callback",methods=["post"])
async def callback():
    try:
        callback_payload = request.get_json()
        print("callback_payload",callback_payload)
        return "callback"

    except Exception as e:
        traceback.print_exc()
    return {"status": "ok"}

# if "__main__" == __name__:
#     app.run()