MESSAGE_PAYLOAD = { "phone": "",
                    "media": {"type": "interactive_reply",
                            "header": {"text": "Request for Consent" },
                                            "body": "HI {}, Do you Want to Exchange visiting card with {}", "footer_text": "c@2021", "button": [ { "id": "56", "title": "Yes" }, { "id": "55", "title": "No" },{ "id": "55", "title": "Spam" } ] } }


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

SIMPLEPAYLOAD ={
    "phone": "",
    "text": "Hello  from test"
}

#old callback payload sample for reference
# CALLBACK_PAYLOAD = {"contacts": [{"profile": {"name": "Sheetal kashid"}, "wa_id": "919152762343"}],
# "messages": [{"context": {"from": "918928894215", "id": "gBEGkZdpGHlyAgnPMbN9MQqIicA"},
# "from": "919769187972", "id": "7131d830-4161-11ec-92a2-0242ac120007",
# "interactive": {"button_reply": {"id": "", "title": "Yes"},
# "type": "button_reply"}, "timestamp": "1636464730", "type": "interactive"}], "brand_msisdn": "918928894215", "request_id": "7131d830-4161-11ec-92a2-0242ac120007", "username": "demo", "user_contact": "+919769187972"} 


RCS_PAYLOAD = {
	"type": "card",
	"phone_no": "",
	"bot_name": "Routemobile",
	"card": {
		"title": "",
		"description": "You can contact via",
		"url": "https://image.freepik.com/free-photo/business-card-stack-mockup_23-2147687412.jpg",
		"suggestions": [{
			"type":"url",
			"text":"",
			"url":"",
			"postback":"url"
		},
        {
			"type":"url",
			"text":"",
			"url":"",
			"postback":"url"
		},
            {	"type":"dial",
			"text":"",
			"call_to":"",
			"postback":"Call us"
		}
		]
	}
}


BULKPAYLOAD = {
    "phone": "",
    "media": {
        "type": "image",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg",
        "file": "flower.jpg",
        "caption": "Message From"
    },
    "extra": "sampleim"
}
