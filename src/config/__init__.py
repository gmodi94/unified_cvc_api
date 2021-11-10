MESSAGE_PAYLOAD = { "phone": "",
                    "media": {"type": "interactive_reply",
                            "header": {"type": "video",
                                            "url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
                                            "file": "pdf.pdf",
                                            "caption": "This is a test video" },
                                            "body": "HI {}, Do you Want to Exchange visiting card with {}", "footer_text": "c@2021", "button": [ { "id": "56", "title": "Yes" }, { "id": "55", "title": "No" } ] } }


RICH_TEXT_PAYLOAD ={
    "phone": "",
    "media": {
        "type": "image",
        "url": "https://image.freepik.com/free-photo/business-card-stack-mockup_23-2147687412.jpg",
        "file": "image.jpg",
        "caption":"Contact Details Received From {}: \n *Name:* {} \n *Mobile Number:* {} \n *Company Name:* Route Mobile Limited \n *Designation:* Software Developer \n *Address:* {}"
    }

}

FALLBACK_PAYLOAD = {
        "phone":"",
        "fallback_text":"Sorry!! Please connect me later. Thank You."
}


#old callback payload sample for reference
CALLBACK_PAYLOAD = {"contacts": [{"profile": {"name": "Sheetal kashid"}, "wa_id": "919152762343"}],
"messages": [{"context": {"from": "918928894215", "id": "gBEGkZdpGHlyAgnPMbN9MQqIicA"},
"from": "919769187972", "id": "7131d830-4161-11ec-92a2-0242ac120007",
"interactive": {"button_reply": {"id": "", "title": "Yes"},
"type": "button_reply"}, "timestamp": "1636464730", "type": "interactive"}], "brand_msisdn": "918928894215", "request_id": "7131d830-4161-11ec-92a2-0242ac120007", "username": "demo", "user_contact": "+919769187972"}
