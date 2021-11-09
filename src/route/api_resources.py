from main import app
from flask import request,jsonify

from utils.decorators import middleware

@app.route("/v1/scan",methods=["post"])
@middleware
async def scan(user_id):
    payload = request.get_json()
    print(user_id)
    
    if payload.get("id","")=="":
        return jsonify({"status":False})

    send_message(config.Sendcosent,)
    return jsonify({"status":True})
    


# if "__main__" == __name__:
#     app.run()