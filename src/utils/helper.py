import io
import qrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import base64
def qr(id, first_name, last_name ):
    image = Image.new('RGB',(400,500),(255,255,255))
    # Logo_link = 'unified_cvc_api/src/utils/cvc.jpeg'
    # logo = Image.open(Logo_link)
    basewidth = 40
    # wpercent = (basewidth/float(logo.size[0]))
    # hsize = int((float(logo.size[1])*float(wpercent)))
    # logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(id)
    QRcode.make()
    QRcolor = 'Black'
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')
    # pos = ((QRimg.size[0] - logo.size[0]) // 2,
        # (QRimg.size[1] - logo.size[1]) // 2)
    # QRimg.paste(logo, pos)
    image.paste(QRimg,(50,70))
    draw = ImageDraw.Draw(image)
    text2 = 'Visiter ID'
    font = ImageFont.load_default()
    draw.text((130, 50), text2, fill='Red',font=font)
    text = f'Name : {first_name} {last_name}'
    text2 = 'Visiter ID'
    font = ImageFont.load_default()
    draw.text((90, 350), text, fill='black',font=font)
    stream =io.BytesIO()
    image.save(stream ,format="png")
    blobdata = stream.getvalue()
    blobdata = base64.b64encode(blobdata)
    # print(base64.b64encode(blobdata))
    return blobdata
    
def create_blob():
    image_file = open('hi.png','rb').read()
    blob_data = base64.b64encode(image_file)
    return blob_data