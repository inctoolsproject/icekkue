import errno
import os
import sys
import tempfile
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('f2ZAIRDhyaMMmmhPB1G8BQDZjzFc2aTM2g1Y5J9jWliY0M4+gMhYzzTrDm9Os1aUv7oKIetsvYetYwlmuiGj4deDwfKFQOeKcnMlhMkubwpUmZCfojqzQS10+vVZC89KRA3uLIuz/ObEFaXWf0UaUgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ed773ebfcd44875532c32f39ff494158')
#-------------{ REMAKE }-------------#

notes = {}
tokenz = {}


# Post Request

@app.route("/callback", methods=['POST'])

def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
    
@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Type /help for command :D\n\nFollow My Creator To Ask Questions -_-\nhttps://line.me/ti/p/zIlrfDTGAo')) 

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get user_id
    gid = event.source.sender_id #get group_id
    
#-------------{ NOTHING }-------------#
    if text == '/bsybye':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Pamit dulu bye-bye'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Pamit dulu bye-bye'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
#-------------{ REMAKE }-------------#
    if text == "redtube on":
    	r = request.get_data('https://api.eater.pw/redtube?page=1')
    	data=r.text
    	data=json.loads(data)
    	for anu in data["result"]:
        	line_bot_api.reply_message(event.reply_token,VideoMessage(original_content_url=anu["dl"], preview_image_url=anu["img"]))
        
    elif text == "xvideos on":
    	r = request.get_data('https://api.eater.pw/xvideos?page=1')
    	data=r.text
    	data=json.loads(data)
    	for anu in data["result"]:
    		line_bot_api.reply_message(event.reply_token,VideoMessage(original_content_url=anu["dl"], preview_image_url=anu["img"]))
#-------------{ REMAKE }-------------#
    elif text == 'confirm':
        confirm_template = ConfirmTemplate(text='Bot nya bagus?', actions=[
            MessageTemplateAction(label='Yes', text='Yes!'),
            MessageTemplateAction(label='No', text='No!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)

    elif "/idline: " in event.message.text:
        skss = event.message.text.replace('/idline: ', '')
        sasa = "http://line.me/R/ti/p/~" + skss
        text_message = TextSendMessage(text=sasa)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0

    elif "/artinama: " in event.message.text:
        skss = event.message.text.replace('/artinama: ', '')
        url = requests.get("https://rest.farzain.com/api/nama.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&q="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["result"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/zodiac: " in event.message.text:
        skss = event.message.text.replace('/zodiac: ', '')
        url = requests.get("https://triopekokbots026.herokuapp.com/zodiak="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["result"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/tr-th: " in event.message.text:
        skss = event.message.text.replace('/tr-th: ', '')
        url = requests.get("https://ryns-api.herokuapp.com/translate?&to=th&text="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["text"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/tr-en: " in event.message.text:
        skss = event.message.text.replace('/tr-en: ', '')
        url = requests.get("https://ryns-api.herokuapp.com/translate?&to=en&text="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["text"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/tr-ar: " in event.message.text:
        skss = event.message.text.replace('/tr-id: ', '')
        url = requests.get("https://ryns-api.herokuapp.com/translate?&to=ar&text="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["text"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/tr-id: " in event.message.text:
        skss = event.message.text.replace('/tr-id: ', '')
        url = requests.get("https://ryns-api.herokuapp.com/translate?&to=id&text="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["text"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/acaratv: " in event.message.text:
        skss = event.message.text.replace('/acaratv: ', '')
        url = requests.get("https://rest.farzain.com/api/acaratv.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&id="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["result"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/shorturl: " in event.message.text:
        skss = event.message.text.replace('/shorturl: ', '')
        url = requests.get("https://rest.farzain.com/api/url.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&id="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["url"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/fs1: " in event.message.text:
        skss = event.message.text.replace('/fs1: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=rambu&text=' + skss,
        preview_image_url='https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=rambu&text=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/fs2: " in event.message.text:
        skss = event.message.text.replace('/fs2: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=rambu&text=' + skss,
        preview_image_url='https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=rambu&text=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/graffiti: " in event.message.text:
        skss = event.message.text.replace('/graffiti: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/photofunia/graffiti_wall.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&text2=Gans&text1=' + skss,
        preview_image_url='https://rest.farzain.com/api/photofunia/graffiti_wall.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&text2=Gans&text1=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/audio: " in event.message.text:
        skss = event.message.text.replace('/audio: ', '')
        message = AudioSendMessage(
        original_content_url=skss,
        duration=1000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/video: " in event.message.text:
        skss = event.message.text.replace('/video: ', '')
        message = VideoSendMessage(
        original_content_url=skss,
        preview_image_url=skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/image: " in event.message.text:
        skss = event.message.text.replace('/image: ', '')
        message = ImageSendMessage(
        original_content_url=skss,
        preview_image_url=skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/linepost: " in event.message.text:
        skss = event.message.text.replace('/linepost: ', '')
        url = requests.get("https://rest.farzain.com/api/special/line.php?&apikey=vhbotsline&id="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["result"],
        preview_image_url=data["result"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/youtubemp4: " in event.message.text:
        skss = event.message.text.replace('/youtubemp4: ', '')
        url = requests.get("https://api.boteater.co/youtube?url="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["result"][0]["link"],
        preview_image_url=data["result"][0]["link"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/youtubemp3: " in event.message.text:
        skss = event.message.text.replace('/youtubemp3: ', '')
        url = requests.get("https://api.boteater.co/youtube?url="+ skss)
        data = url.json()
        message = AudioSendMessage(
        original_content_url=data["result"][0]["link"],
        duration=1000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/smulevideo: " in event.message.text:
        skss = event.message.text.replace('/smulevideo: ', '')
        url = requests.get("https://triopekokbots026.herokuapp.com/downloadsmule="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["result"][0]["url"],
        preview_image_url=data["result"][0]["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/smuleaudio: " in event.message.text:
        skss = event.message.text.replace('/smuleaudio: ', '')
        url = requests.get("https://triopekokbots026.herokuapp.com/downloadsmule="+ skss)
        data = url.json()
        message = AudioSendMessage(
        original_content_url=data["result"][0]["url"],
        duration=1000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/music: " in event.message.text:
        skss = event.message.text.replace('/music: ', '')
        url = requests.get("https://arsybai.herokuapp.com/rest/soundcloud?apikey=Paijo&query="+ skss)
        data = url.json()
        message = AudioSendMessage(
        original_content_url=data["result"][0]["audio"],
        duration=1000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/light: " in event.message.text:
        skss = event.message.text.replace('/light: ', '')
        url = requests.get("http://api.zicor.ooo/graffiti.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/street: " in event.message.text:
        skss = event.message.text.replace('/street: ', '')
        url = requests.get("http://api.zicor.ooo/streets.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/cookies: " in event.message.text:
        skss = event.message.text.replace('/cookies: ', '')
        url = requests.get("http://api.zicor.ooo/wcookies.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/sletters: " in event.message.text:
        skss = event.message.text.replace('/sletters: ', '')
        url = requests.get("http://api.zicor.ooo/sletters.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/goimage: " in event.message.text:
        skss = event.message.text.replace('/goimage: ', '')
        url = requests.get("https://api.eater.pw/googleimg?search="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["result"][0]["img"],
        preview_image_url=data["result"][0]["img"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    elif "/apakah " in event.message.text:
        quo = ('Iya','Tidak','Gak tau','Bisa jadi','Mungkin iya','Mungkin tidak')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
        
    if text == '/tiktok':
        url = requests.get("https://rest.farzain.com/api/tiktok.php?country=jp&apikey=3w92e8nR5eWuDWQShRlh6C1ye&type=json")
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["first_video"],
        preview_image_url=data["first_video"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/xvideos: " in event.message.text:
        skss = event.message.text.replace('/xvideos: ', '')
        url = requests.get("https://api.boteater.co/xvideos?page="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["result"]["dl"],
        preview_image_url=data["result"]["dl"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    elif (text == 'Bot') or (text == 'bot'):
        message = TextSendMessage(text='Siapa bot? ke bot an lu')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Ping') or (text == 'ping'):
        message = TextSendMessage(text='Pong 􀨁􀄻mantap􏿿')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Respon') or (text == 'respon'):
        message = TextSendMessage(text='Hadir 􀠁􀅢adaapa?􏿿')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Rname') or (text == 'rname'):
        message = TextSendMessage(text='「 ᴛʀɪᴏ ᴘᴇᴋᴏᴋ ʙᴏᴛs 」')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Sp') or (text == '.sp') or (text == 'Speed') or (text == '/sp') or (text == '.speed'):
        message = TextSendMessage(text='「 0.003705247497558544 」 second')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mid') or (text == 'mid') or (text == 'Mymid') or (text == 'mymid') or (text == '.mid'):
        message = TextSendMessage(text=event.source.user_id)
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Gid') or (text == 'gid') or (text == 'Groupid') or (text == 'groupid') or (text == '.gid'):
        message = TextSendMessage(text=event.source.sender_id)
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/lokasi') or (text == 'Mylokasi'):
        message = LocationSendMessage(
        title='my location',
        address='Gg. Tentrem, Pasuruhan Lor, Jati, Kabupaten Kudus, Jawa Tengah 59349, Indonesia',
        latitude=-6.8172919,
        longitude=110.8217371
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/bmkg') or (text == 'Bmkg'):
        url = requests.get("https://triopekokbots026.herokuapp.com/bmkg")
        data = url.json()
        message = TextSendMessage(text=data["info"])
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ Credit by @Basyir? }-------------#
    elif (text == '/chromeos') or (text == 'Chromeos'):
        url = requests.get("https://api.eater.pw/token?header=CHROMEOS")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 ᴛʀɪᴏ ᴘᴇᴋᴏᴋ ʙᴏᴛs 」\nKlik Link Dibawah Ini Untuk Login Token Chrome\n'+bsyr)
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/iosipad') or (text == 'Iosipad'):
        url = requests.get("https://api.eater.pw/token?header=IOSIPAD")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 ᴛʀɪᴏ ᴘᴇᴋᴏᴋ ʙᴏᴛs 」\nKlik Link Dibawah Ini Untuk Login Token Iosipad\n'+bsyr)
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/desktopmac') or (text == 'Desktopmac'):
        url = requests.get("https://api.eater.pw/token?header=DESKTOPMAC")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 ᴛʀɪᴏ ᴘᴇᴋᴏᴋ ʙᴏᴛs 」\nKlik Link Dibawah Ini Untuk Login Token Desktopmac\n'+bsyr)
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/desktopwin') or (text == 'Desktopwin'):
        url = requests.get("https://api.eater.pw/token?header=DESKTOPWIN")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 ᴛʀɪᴏ ᴘᴇᴋᴏᴋ ʙᴏᴛs 」\nKlik Link Dibawah Ini Untuk Login Token Desktopwin\n'+bsyr)
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/win10') or (text == 'Win10'):
        url = requests.get("https://api.eater.pw/token?header=WIN10")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 ᴛʀɪᴏ ᴘᴇᴋᴏᴋ ʙᴏᴛs 」\nKlik Link Dibawah Ini Untuk Login Token Win10\n'+bsyr)
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/clova') or (text == 'Clova'):
        url = requests.get("https://api.eater.pw/token?header=CLOVAFRIENDS")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 ᴛʀɪᴏ ᴘᴇᴋᴏᴋ ʙᴏᴛs 」\nKlik Link Dibawah Ini Untuk Login Token Clova\n'+bsyr)
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/done') or (text == 'Done Login'):
        data = tokenz[event.source.user_id]
        cok = requests.get(url = data)
        asu = cok.text
        message = TextSendMessage(text=asu)
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ Credit by @Basyir? }-------------#
    elif (text == '/help') or (text == 'help') or (text == 'Help'):
        buttons_template = TemplateSendMessage(
            alt_text='Help message',
            template=ButtonsTemplate(
                thumbnail_image_url='https://media.giphy.com/media/OpMk33frgcs4o/giphy.gif',
                title='HELP COMMAND',
                text= 'Select one menu',
                align= 'center',
                actions=[
                    MessageTemplateAction(
                        label='Media',
                        text='/media'
                    ),
                    MessageTemplateAction(
                        label='List token',
                        text='/list token'
                    ),
                    MessageTemplateAction(
                        label='Bye Bot',
                        text='/bsybye'
                    ),
                    MessageTemplateAction(
                        label='About',
                        text='TRIO PEKOK BOTS\nVERSION BETA TEST\n\nTHANKS TO :\n1. ALLAH SWT\n2. KAWAN KAWAN SEMUA\n3. PARA HATTERS\n4. PARA MANTAN\n5. PARA MUSUH\nTHANK YOU FOR ALL\nTANPA KALIAN AKU BUKAN APA APA\n\nSUPPORT BY :\n1.PASUKAN GAGAL MOVE ON\n2. NF BOTS\n3. PEKOK BOTS\n\nCONTACT ME :\nhttps://line.me/ti/p/zIlrfDTGAo'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
#-------------{ REMAKE }-------------#
    elif text == '/list token':
        message = TemplateSendMessage(
            alt_text='GET TOKEN BOT',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/FB5EOw0CaaQM0/giphy.gif',
                        title='LOGIN CHROMEOS',
                        text='Klik Link Sebelum 2 menit',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/chromeos'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/okWCAjMp0pInC/giphy.gif',
                        title='LOGIN IOSIPAD',
                        text='Klik Link Sebelum 2 menit',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/iosipad'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/Elie14Y5mbi9y/giphy.gif',
                        title='LOGIN DESKTOPMAC',
                        text='Klik Link Sebelum 2 menit',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/desktopmac'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/Xhwv0kw43N5MA/giphy.gif',
                        title='LOGIN DESKTOPWIN',
                        text='Klik Link Sebelum 2 menit',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/desktopwin'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/2jF83vAvri1SE/giphy.gif',
                        title='LOGIN WIN10',
                        text='Klik Link Sebelum 2 menit',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/win10'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/TgrljVi87D3rO/giphy.gif',
                        title='LOGIN CLOVAFRIENDS',
                        text='Klik Link Sebelum 2 menit',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/clova'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ REMAKE }-------------#
    elif text == '/media':
        message = TemplateSendMessage(
            alt_text='GET TOKEN BOT',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/FB5EOw0CaaQM0/giphy.gif',
                        title='YOUTUBE',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/getyoutube'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/okWCAjMp0pInC/giphy.gif',
                        title='SEARCH MUSIC',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/music:%20Ku%20tak%20pantas%20disurga'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/8Lc5xmvzRhlLy/giphy.gif',
                        title='SMULE DOWNLOAD',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/getsmule'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/MlTMwvO9ZiWwU/giphy.gif',
                        title='ZODIAC',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/zodiac:%20leo'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/H5AMoAO4JLPEI/giphy.gif',
                        title='INFO BMKG',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/bmkg'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/Elie14Y5mbi9y/giphy.gif',
                        title='TRANSLATE',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/gettranslate'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/Xhwv0kw43N5MA/giphy.gif',
                        title='IMAGE TEXT',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/getimage'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/2jF83vAvri1SE/giphy.gif',
                        title='DOWNLOAD TIMELINE',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/linepost:%20https://timeline.line.me/post/_ddY6q2YVLnhXL9v3_7uZoCY9MCGK5XJJSdWwKEw/1153943773206072460'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/TgrljVi87D3rO/giphy.gif',
                        title='CHECKING',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/getchecking'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ REMAKE }-------------#
    elif (text == '/creator') or (text == 'About'):
        message = TemplateSendMessage(
            alt_text='Cuma Hoax Kok',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/yuQkwlSrSUjmw/giphy.gif',
                        title='MY ACCOUNT',
                        text='Click to get acquainted',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='https://line.me/ti/p/zIlrfDTGAo'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/PNiglq4bMV94c/giphy.gif',
                        title='MY SECONDARY ACCOUT',
                        text='Click to follow',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='https://line.me/ti/p/buz6KFKzad'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/PSnmIFuLsf960/giphy.gif',
                        title='OFFICIAL ACCOUNT',
                        text='Click to follow',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='http://line.me/ti/p/%40swv6521a'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ REMAKE }-------------#
    elif (text == '/getsmule'):
        message = TemplateSendMessage(
            alt_text='SMULE DOWNLOADER',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/2jF83vAvri1SE/giphy.gif',
                        title='DOWNLOAD SMULE AUDIO',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/smuleaudio:%20https://www.smule.com/p/891883466_2593667160'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/6ClI61nEYQ8Lu/giphy.gif',
                        title='DOWNLOAD SMULE VIDEO',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/smulevideo:%20https://www.smule.com/p/891883466_2561918198'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ REMAKE }-------------#
    elif (text == '/getyoutube'):
        message = TemplateSendMessage(
            alt_text='YOUTUBE DOWNLOADER',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/2jF83vAvri1SE/giphy.gif',
                        title='DOWNLOAD YOUTUBE AUDIO',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/youtubemp3:%20https://youtu.be/GaeaVm3PI1A'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/6ClI61nEYQ8Lu/giphy.gif',
                        title='DOWNLOAD YOUTUBE VIDEO',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/youtubemp4:%20https://youtu.be/GaeaVm3PI1A'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ REMAKE }-------------#
    elif (text == '/gettranslate'):
        message = TemplateSendMessage(
            alt_text='TRANSLATE LEAGUE',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/2jF83vAvri1SE/giphy.gif',
                        title='TRANSLATE THAILAND',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/tr-th:%20Sepertinya%20Aku%20Homo'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/TgrljVi87D3rO/giphy.gif',
                        title='TRANSLATE ARAB',
                        text='Click to follow',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/tr-ar:%20Sepertinya%20Aku%20Homo'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/a3wq0KrRi6e76/giphy.gif',
                        title='TRANSLATE INGGRIS',
                        text='Click to follow',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/tr-en:%20Sepertinya%20Aku%20Homo'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/6ClI61nEYQ8Lu/giphy.gif',
                        title='TRANSLATE INDONESIA',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/tr-id:%20Looks%20i%20am%20Homo'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ REMAKE }-------------#
    elif text == '/getimage':
        message = TemplateSendMessage(
            alt_text='IMAGE TEXT',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/FB5EOw0CaaQM0/giphy.gif',
                        title='FANSIGN 1',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/fs1:%20TESTING'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/okWCAjMp0pInC/giphy.gif',
                        title='FANSIGN 2',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/fs2:%20TESTING'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/H10tCrEZDhbBm/giphy.gif',
                        title='GRAFFITI',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/graffiti:%20TESTING'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/kC5uaiZfzkvra/giphy.gif',
                        title='LIGHT',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/light:%20TESTING'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/aDMBVa9FqX7Jm/giphy.gif',
                        title='STREET',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/street:%20TESTING'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/Elie14Y5mbi9y/giphy.gif',
                        title='COOKIES',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/cookies:%20TESTING'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/Xhwv0kw43N5MA/giphy.gif',
                        title='SLETTERS',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/sletters:%20TESTING'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/TgrljVi87D3rO/giphy.gif',
                        title='GOOGLE IMAGE',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=/goimage:%20naruto'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ REMAKE }-------------#
    elif (text == '/getchecking'):
        message = TemplateSendMessage(
            alt_text='CHECKING',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/2jF83vAvri1SE/giphy.gif',
                        title='IMAGE',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=foimage&img=https://i.ibb.co/Tr1mjYH/1545946474474.jpg'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/TgrljVi87D3rO/giphy.gif',
                        title='AUDIO',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=audio&link=https://platelets.fun/public/sounds/music.mp3'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/6ClI61nEYQ8Lu/giphy.gif',
                        title='VIDEO',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=video&ocu=https://tinyurl.com/y8og3or5&piu=https://tinyurl.com/y8og3or5'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ REMAKE }-------------#
    elif (text == '/app'):
        message = TemplateSendMessage(
            alt_text='LIST APLIKASI',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/2jF83vAvri1SE/giphy.gif',
                        title='LINE',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=https://drive.google.com/file/d/1C9HApH1D-f60KRFVsTBhAXspFQg25ZZ8/view?usp=drivesdk'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/m3SosS7kjWInu/giphy.gif',
                        title='CREATE FANCYNAME',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=https://drive.google.com/file/d/1bLA28as0LztPNO1x28TeK1Xm3jnKXn5q/view?usp=drivesdk'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/TgrljVi87D3rO/giphy.gif',
                        title='ES FILE EXPLORER PRO',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=http://rexdlfile.com/index.php?id=es-file-explorer-pro-apk'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.giphy.com/media/6ClI61nEYQ8Lu/giphy.gif',
                        title='MULTI PRO',
                        text='© Relax and enjoy your quest',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='line://app/1636361179-N9dnRpYg?type=fotext&text=https://m.apkpure.com/id/multiple-account-pro/workersdesign.dualaccountpro'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ REMAKE }-------------#
    elif (text == '/me') or (text == 'Me') or (text == '.me'):
        message = TemplateSendMessage(
            alt_text='Cuma Hoax Kok',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.ibb.co/gVxvZfq/20190302-224956.png',
                        title='Name: ' + line_bot_api.get_profile(event.source.user_id).display_name,
                        text='Status: '+ line_bot_api.get_profile(event.source.user_id).status_message,
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='https://line.me/ti/p/zIlrfDTGAo'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
#-------------{ REMAKE }-------------#
    elif (text == 'makasih') or (text == 'Makasih'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/21831487/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Nah') or (text == 'Nahh'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/37652126/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Matamu') or (text == 'Matane'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/7111997/IOS/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hoax') or (text == 'Hoaxx'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/11221543/IOS/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hmm') or (text == 'Hm'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/18423382/IOS/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    elif (text == 'Drama') or (text == 'Eleh'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/34558069/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'nyimak') or (text == 'Nyimak'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/9756022/IOS/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'ga') or (text == 'gak') or (text == 'gamau') or (text == 'Gamau') or (text == 'Ga') or (text == 'Gak'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683557/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Keren') or (text == 'Mantap') or (text == 'Kerenn') or (text == 'Mantapp') or (text == 'Bagus') or (text == 'Hebat'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12860202/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sepi'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200512/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Malem') or (text == 'Met malem'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/18282481/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Hai') or (text == 'Halo'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186953/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'sabar') or (text == 'Sabar'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22499899/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Ngantuk'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691708/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Haha') or (text == 'Wkwk'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200499/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Kzl') or (text == 'Kezel'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24464008/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Go') or (text == 'Siap'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186952/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif text == 'Bingung':
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/34751035/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Tolong') or (text == 'Please'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/11825345/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Okee') or (text == 'Okay') or (text == 'Ok') or (text == 'Oke'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22482252/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Baper') or (text == 'Karepmu'):
        message = TemplateSendMessage(
            alt_text='TRIO PEKOK PROTECTION',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16365505/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kamm') or (text == 'Kam') or (text == 'Wc') or (text == 'Welcome'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24862265/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bye') or (text == 'Minggat'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/34558071/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Ngopi') or (text == 'Ngopii') or (text == 'Ngopi cok') or (text == 'Ngopi woy'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691714/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Opo') or (text == 'Opoo') or (text == 'Naon'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691705/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Jancik') or (text == 'Jancok') or (text == 'Jancuk') or (text == 'Ancik'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547155/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sider on') or (text == 'Cctv on') or (text == 'Lurking on') or (text == '.sider on'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200507/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Mandi') or (text == 'Adus') or (text == 'Mandi dulu') or (text == 'Adus sik'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691709/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Juhh') or (text == 'Johh') or (text == 'Juoh'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12521487/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hbd') or (text == 'Met ultah') or (text == 'Selamat hari jadi') or (text == 'Happy Birthday'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/7670129/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Salken') or (text == 'Salam kenal'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24464015/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'O') or (text == 'O aja') or (text == 'Oo') or (text == 'Ooo'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/17530681/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Gift') or (text == 'Gift aku') or (text == 'Gift me') or (text == 'Gift dul'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22220762/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Dih'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12842266/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Yank') or (text == 'Syg') or (text == 'Jo'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/78960399/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'No') or (text == 'Tidak Boleh') or (text == 'Moh') or (text == 'Giah'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12842265/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Galau') or (text == 'Galon') or (text == 'Lagi galon') or (text == 'Lagi galau'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/55737941/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kenyang') or (text == 'Wareg'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12842261/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == '$me') or (text == 'Me') or (text == '.me') or (text == '!me'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16673425/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Maaf') or (text == 'Sorry'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/18282476/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Muleh'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/20217667/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Mbalik'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547168/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Jembut') or (text == 'Asw') or (text == 'Jiembut') or (text == 'Asu'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200497/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Otw') or (text == 'Otww') or (text == 'Gas'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/20217665/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sue') or (text == 'Suee') or (text == 'Suek') or (text == 'Sueek'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/19002665/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == '@?????????Rizal??????? ') or (text == 'Rizal') or (text == 'Zal') or (text == 'Mbot'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/14038591/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == '@??????????ARDEWI)????? ') or (text == 'Botak') or (text == 'Ari') or (text == 'Tak'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/17354215/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == '@??????????????????? ') or (text == 'Manyun') or (text == 'Nyun'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/14038579/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == '@(???????????????????)') or (text == 'Syir') or (text == 'Sir') or (text == 'Basyir'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186955/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Pm') or (text == 'Pc') or (text == 'Cek pm') or (text == 'Buka pm'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/17241274/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kuy') or (text == 'Kuyy') or (text == 'Kuy ah') or (text == 'Kuyy ah'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200506/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bubug') or (text == 'Bobog') or (text == 'Tidur') or (text == 'Merem'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/26538903/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Apes') or (text == 'Apes aku'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200515/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Pekok') or (text == 'Gemblung') or (text == 'Koplok') or (text == 'Gendeng'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12521475/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sepi') or (text == 'Sepii'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200512/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Makan') or (text == 'Mangan') or (text == 'Maem'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/14038588/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    elif (text == 'Jones') or (text == 'Jomblo') or (text == 'Mblo'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186956/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Pagi') or (text == 'Met pagi') or (text == 'Morning'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/15666186/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bangun') or (text == 'Tangi'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547152/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Terserah') or (text == 'Serah'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691717/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Call') or (text == 'Kojom') or (text == 'Ayo kojom'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200511/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Wekkk') or (text == 'Wekk') or (text == 'Wek'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547171/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kangen') or (text == 'Angen') or (text == 'Kangenn'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/11866860/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Muah') or (text == 'Muach') or (text == 'Muachhh'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691710/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hihi') or (text == 'Hihihi') or (text == 'Hihihihi'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186955/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Typo') or (text == 'Asem typo') or (text == 'Typoo'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547158/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bacot') or (text == 'Omong ae') or (text == 'Padon ae'):
        message = TemplateSendMessage(
            alt_text='Sorry this is just a sticker',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/23581910/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/zIlrfDTGAo')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ Credit by @Basyir? }-------------#

import os

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
