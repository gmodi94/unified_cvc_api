MESSAGE_PAYLOAD = { "phone": "",
                    "media": {"type": "interactive_reply",
                            "header": {"text": "Request for Consent" },
                                            "body": "HI {}, Do you Want to Exchange visiting card with {}", "footer_text": "c@2021", "button": [ { "id": "56", "title": "Yes" }, { "id": "55", "title": "No" } ] } }


RICH_TEXT_PAYLOAD ={
    "phone": "",
    "media": {
        "type": "image",
        "url": "https://image.freepik.com/free-photo/business-card-stack-mockup_23-2147687412.jpg",
        "file": "image.jpg",
        "caption":""
    }

}

FALLBACK_PAYLOAD = {
        "phone":"",
        "text":""
}


#old callback payload sample for reference
# CALLBACK_PAYLOAD = {"contacts": [{"profile": {"name": "Sheetal kashid"}, "wa_id": "919152762343"}],
# "messages": [{"context": {"from": "918928894215", "id": "gBEGkZdpGHlyAgnPMbN9MQqIicA"},
# "from": "919769187972", "id": "7131d830-4161-11ec-92a2-0242ac120007",
# "interactive": {"button_reply": {"id": "", "title": "Yes"},
# "type": "button_reply"}, "timestamp": "1636464730", "type": "interactive"}], "brand_msisdn": "918928894215", "request_id": "7131d830-4161-11ec-92a2-0242ac120007", "username": "demo", "user_contact": "+919769187972"} 


RCS_PAYLOAD = {
	"type": "card",
	"phone_no": "+919082366048",
	"bot_name": "Routemobile",
	"card": {
		"title": "Bussiness Card",
		"description": "The description for card #2",
		"url": "https://storage.googleapis.com/kitchen-sink-sample-images/cute-dog.jpg",
		"suggestions": [{
			"type":"url",
			"text":"Tap me",
			"url":"http://wa.me/+919082366048",
			"postback":"url"
		},
        {
			"type":"url",
			"text":"Tap me",
			"url":"https://conviscard.herokuapp.com/mail?mail=waghela.rutvej1@gmail.com",
			"postback":"url"
		},
            {	"type":"dial",
			"text":"Call us",
			"call_to":"+919082366048",
			"postback":"Call us"
		}
		]
	}
}
