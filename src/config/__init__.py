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

RCS_BULK_PAYLOAD = {
	"type": "card",
	"phone_no": "",
	"bot_name": "Routemobile",
	"card": {
		"title": "",
		"description": "Look my new service",
		"url": ""}

}


MAIL_PAYLOAD ={
    "smtp_user_name": "smtp50438253",
    "message": {
        "html": "<!--Download - https://github.com/lime7/responsive-html-template.git--> <html lang='en'> <head> <meta charset='UTF-8'> <meta http-equiv='X-UA-Compatible' content='IE=edge' /> <title>One Letter</title> <meta name='viewport' content='width=device-width, initial-scale=1.0'/> <style> .ReadMsgBody {width: 100%; background-color: #ffffff;} .ExternalClass {width: 100%; background-color: #ffffff;} /* Windows Phone Viewport Fix */ @-ms-viewport { width: device-width; } </style> <!--[if (gte mso 9)|(IE)]> <style type='text/css'> table {border-collapse: collapse;} .mso {display:block !important;} </style> <![endif]--> </head> <body leftmargin='0' topmargin='0' marginwidth='0' marginheight='0' style='background: #e7e7e7; width: 100%; height: 100%; margin: 0; padding: 0;'> <!-- Mail.ru Wrapper --> <div id='mailsub'> <!-- Wrapper --> <center class='wrapper' style='table-layout: fixed; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; padding: 0; margin: 0 auto; width: 100%; max-width: 960px;'> <!-- Old wrap --> <div class='webkit'> <table cellpadding='0' cellspacing='0' border='0' bgcolor='#ffffff' style='padding: 0; margin: 0 auto; width: 100%; max-width: 960px;'> <tbody> <tr> <td align='center'> <!-- Start Section (1 column) --> <table id='intro' cellpadding='0' cellspacing='0' border='0' bgcolor='#4F6331' align='center' style='width: 100%; padding: 0; margin: 0; background-image: url(https://github.com/lime7/responsive-html-template/blob/master/index/intro__bg.png?raw=true); background-size: auto 102%; background-position: center center; background-repeat: no-repeat; background-color: #080e02'> <tbody > <tr><td colspan='3' height='20'></td></tr> <tr> <td width='330' style='width: 33%;'></td> <!-- Main Title --> <tr> <td colspan='3' height='60' align='center'> <br> <br> <br> <br> <br> <br> <br> <div border='0' style='border: none; line-height: 60px; color: #ffffff; font-family: Verdana, Geneva, sans-serif; font-size: 52px; text-transform: uppercase; font-weight: bolder;'>Thank, You!</div> </td> </tr> <!-- Line 1 --> <tr> <td colspan='3' height='20' valign='bottom' align='center'> <img src='https://github.com/lime7/responsive-html-template/blob/master/index/line-1.png?raw=true' alt='line' border='0' width='464' height='5' style='border: none; outline: none; max-width: 464px; width: 100%; -ms-interpolation-mode: bicubic;' > </td> </tr> <!-- Meta title --> <tr> <td colspan='3'> <table cellpadding='0' cellspacing='0' border='0' align='center' style='padding: 0; margin: 0; width: 100%;'> <tbody> <tr> <td width='90' style='width: 9%;'></td> <td align='center'> <div border='0' style='border: none; height: 60px;'> <p style='font-size: 18px; line-height: 24px; font-family: Verdana, Geneva, sans-serif; color: #ffffff; text-align: center; mso-table-lspace:0;mso-table-rspace:0;'> Thank you for using CVC , Please Find Your Connection in Attachment. </p> </div> </td> <td width='90' style='width: 9%;'></td> </tr> </tbody> </table> </td> </tr> <tr><td colspan='3' height='160'></td></tr> <tr> <td width='330'></td> <!-- Button Start --> <td width='300' align='center' height='52'> <div style='background-image: url(https://github.com/lime7/responsive-html-template/blob/master/index/intro__btn.png?raw=true); background-size: 100% 100%; background-position: center center; width: 225px;'> </div> </td> <td width='330'></td> </tr> <tr><td colspan='3' height='85'></td></tr> </tbody> </table><!-- End Start Section --> <!-- Footer --> <table id='news__article' cellpadding='0' cellspacing='0' border='0' bgcolor='#ffffff' align='center' style='width: 100%; padding: 0; margin: 0; background-color: #ffffff'> <tbody> <tr><td colspan='3' height='23'></td></tr> <tr> <td align='center'> <div border='0' style='border: none; line-height: 14px; color: #727272; font-family: Verdana, Geneva, sans-serif; font-size: 16px;'> 2021 © <a href='https://semenchenkov.github.io/' target='_blank' border='0' style='border: none; outline: none; text-decoration: none; line-height: 14px; font-size: 16px; color: #727272; font-family: Verdana, Geneva, sans-serif; -webkit-text-size-adjust:none;'>CVC</a> </div> </td> </tr> <tr><td colspan='3' height='23'></td></tr> </tbody> </table> <!-- End Footer --> </td> </tr> </tbody> </table> </div> <!-- End Old wrap --> </center> <!-- End Wrapper --> </div> <!-- End Mail.ru Wrapper --> </body> </html>",
        "text": "",
        "subject": "CVC Reports",
        "from_email": "noreply@rapidemail.rmlconnect.net",
        "from_name": "CVC MAIl",
        "to": [
            {
                "email": "waghela.rutvej1@gmail.com",
                "name": "Recipient Name",
                "type": "to"
            }
        ],
        "attachments": [
            {
                "type": "text/plain",
                "name": "myfile.csv",
                "content": ""
            }
        ],
        "headers": {
            "Reply-To": "noreply@rapidemail.rmlconnect.net",
            "X-Unique-Id": "id"
        }
    },
    "owner_id": "32360039",
    "token": "8EuquwYgAt7oT9DzW5etrm6W"
}

BULK_MAIL_PAYLOAD ={
    "smtp_user_name": "smtp50438253",
    "message": {
        "html": "",
        "text": "",
        "subject": "CVC MAIL",
        "from_email": "noreply@rapidemail.rmlconnect.net",
        "from_name": "CVC",
        "to": [
            {
                "email": "waghela.rutvej1@gmail.com",
                "name": "Recipient Name",
                "type": "to"
            }
        ],
        "headers": {
            "Reply-To": "noreply@rapidemail.rmlconnect.net",
            "X-Unique-Id": "id"
        }
    },
    "owner_id": "32360039",
    "token": "8EuquwYgAt7oT9DzW5etrm6W"
}