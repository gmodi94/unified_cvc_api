import io
import qrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import base64
import csv
import json
def qr(id, first_name, last_name ):
    image = Image.new('RGB',(400,500),(255,255,255))
    Logo_link = 'src/utils/cvc.jpeg'
    logo = Image.open(Logo_link)
    basewidth = 40
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    fulldata = json.dumps({
        "id":id,
        "Name":first_name+" "+last_name
    })
    QRcode.add_data(fulldata)
    QRcode.make()
    QRcolor = 'Black'
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    image.paste(QRimg.resize((250, 250)),(70,100))
    draw = ImageDraw.Draw(image)
    text2 = 'Visitor ID'
    font = ImageFont.truetype(r'src/utils/arial.ttf', 25)
    draw.text((140, 50), text2, fill='black',font=font)
    text = f'Name : {first_name} {last_name}'
    font = ImageFont.truetype(r'src/utils/arial.ttf', 25)
    draw.text((80, 380), text, fill='black',font=font)
    stream =io.BytesIO()
    image.save(stream ,format="png")
    blobdata = stream.getvalue()
    blobdata = base64.b64encode(blobdata)
    # print(base64.b64encode(blobdata))
    return blobdata.decode()
    
def create_blob():
    image_file = open('hi.png','rb').read()
    blob_data = base64.b64encode(image_file)
    return blob_data

def csv_to_base64(csvdata):
    f = io.StringIO()
    csv.writer(f).writerows(csvdata)
    data = base64.b64encode(f.getvalue().encode())
    print(data)
    return data

def user_to_vcard(user):
    vcardformat = "BEGIN:VCARD\nVERSION:2.1\nN:{};;;;\nFN:{}\nTEL;HOME:{}\nEMAIL:{}\nADR;HOME:;;{}\nEND:VCARD".format(user.first_name,user.first_name+" "+user.last_name,user.mobile_number,user.email,user.address)
    f = io.StringIO()
    f.write(vcardformat)
    data = base64.b64encode(f.getvalue().encode()).decode()
    datadict = {}
    datadict["type"] = "text/plain"
    datadict["name"] = f"{user.first_name}.vcf"
    datadict["content"] = data
    return datadict
