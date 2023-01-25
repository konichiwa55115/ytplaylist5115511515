import os 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import Client, filters,emoji
from pyrogram.types import Message

import requests
HB = Client(
    "YOUTUBE Bot",
    bot_token = "5393596540:AAHumGAfuBHFi9JnywYpGUvLfmapGaO4Dvc",
    api_id = int(17983098),
    api_hash = "ee28199396e0925f1f44d945ac174f64"
)  

START_TEXT = """
السلام عليكم يا {}, 
هذا بوت لتحميل قوائم تشغيل يوتيوب و فيديوهات يوتيوب 
 فقط أرسل رابط قائمة تشغيل أو رابط فيديو يوتيوب 
🚨  البوت لا يدعم تحميل قوائم التشغيل بصيغة صوتية للأسف 
 🚨 ممنوع استخدام البوت لتحميل الأغاني أو المسلسلات أو الأناشيد الإسلامية أو أي شيء حرام 
لبقية البوتات هنا 
 https://t.me/ibnAlQyyim/1120
 و لدعم استمرار المشروع هنا 
  http://paypal.me/kelectronic89 """

HELP_TEXT = """**
    فقط أرسل رابط أي فيديو يوتيوب و اختر الصيغة والجودة 
    أو أرسل رابط قائمة تشغيل 
"""

ABOUT_TEXT = """
 🤖<b>BOT :YOUTUBE DOWNLOADER </b>
 
 🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT
 
 📢<b>CHANNEL :</b>@ibnAlQyyim
 
 📝<b>Language :</b>  <a href='https://python.org/'>Python3</a>
 
 🧰<b>Frame Work :</b>  <a href='https://pyrogram.org/'>Pyrogram</a>
 
 🤩<b>SOURCE :</b>  <a href='https://youtu.be/xyW5fe0AkXo'>CLICK HERE</a>
 
 
"""


@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True
    )

@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    await update.reply_text(
        text=text,
        disable_web_page_preview=True
    )

@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    await update.reply_text(
        text=text,
        disable_web_page_preview=True
    )
@HB.on_message(filters.command(["source"]))
async def about_message(bot, update):
    text = SOURCE_TEXT
    await update.reply_text(
        text=text,
        disable_web_page_preview=True
    )
import os
import math
import time


async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "[{0}{1}] \n<b>• Percentage :</b> {2}%\n".format(
            ''.join([" ▰" for i in range(math.floor(percentage / 10))]),
            ''.join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))

        tmp = progress + "<b>✅ COMPLETED :</b> {0}\n<b>📂 SIZE :</b> {1}\n<b>⚡️ SPEED :</b> {2}/s\n<b>⏰ ETA :</b> {3}\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text="{}\n{}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n]+'B'

def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

UPLOAD_START = " <bold>Upload STARTED...</bold>"


from pytube import YouTube
VIDEO_REGEX = r'(.*)youtube.com/(.*)[&|?]v=(?P<video>[^&]*)(.*)'
PLAYLIST_REGEX = r'(.*)youtube.com/(.*)[&|?]list=(?P<playlist>[^&]*)(.*)'
@HB.on_message(filters.regex(VIDEO_REGEX))
async def ytdl(_, message):
   l = message.text.split()
   global var
   global ythd
   global ytlow
   global yt
   global song
   global file
   global thumb
   global ytaudio
   var=message.text
   url= message.text
   yt = YouTube(url)
   chat_id =message.chat.id
   thumb = yt.thumbnail_url
   ythd = yt.streams.get_highest_resolution()
   ytlow = yt.streams.get_by_resolution(resolution ='360p')
   file = yt.streams.filter(only_audio=True).first()
   ytaudio = yt.streams.filter(only_audio=True).first()
   download = ytaudio.download(filename=f"{str(yt.title)}")
   rename = os.rename(download, f"{str(yt.title)}.mp3")
   audio_size = f"{int(format_bytes(ytaudio.filesize)[0]):.2f}{format_bytes(ytaudio.filesize)[1]}"
   hd = f"{int(format_bytes(ythd.filesize)[0]):.2f}{format_bytes(ythd.filesize)[1]}"
   low = f"{int(format_bytes(ytlow.filesize)[0]):.2f}{format_bytes(ytlow.filesize)[1]}"
   
   import requests
   result_buttons2 = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('🎬720P ' +' ⭕️ '+ hd, callback_data='high'),
        InlineKeyboardButton('🎬 360p ' + '⭕️ ' +  low, callback_data='360p')
    ],[
        InlineKeyboardButton('🎧 AUDIO '+  '⭕️ ' +  audio_size , callback_data='audio')
    ],[
        InlineKeyboardButton('🖼THUMBNAIL🖼', callback_data='thumbnail')
    ]]
   )
   
   await message.reply_photo(
            photo=thumb,
            caption="🎬 TITLE : "+ yt.title +  "\n\n📤 UPLOADED : " + yt.author  + "\n\n📢 CHANNEL LINK " + f'https://www.youtube.com/channel/{yt.channel_id}',
            reply_markup=result_buttons2,
            quote=True,
    
    )
import time
start_time = time.time()


@HB.on_callback_query()
async def cb_data(bot, update):                     
    
    if update.data == 'high':
     try:
        await  HB.send_video(
            chat_id = update.message.chat.id, 
            video = ythd.download(),
            caption=result_text,
            progress=progress_for_pyrogram,
                    progress_args=(
                        UPLOAD_START,
                        update.message,
                        start_time
                    )
      )
        await update.message.delete()
     except:
        await HB.send_message(
            chat_id = update.message.chat.id,
            text="**😔 1080P QUALITY IS NOT AVAILABLE\n CHOOSE ANY OTHER QUALITIES**")    
    
    elif update.data == '360p':
     try:
      await  HB.send_video(
        chat_id = update.message.chat.id, 
        video = ytlow.download(),
        caption=result_text,
       progress=progress_for_pyrogram,
                    progress_args=(
                        UPLOAD_START,
                        update.message,
                        start_time
                    )
        )
      await update.message.delete()

     except:
        await HB.send_message(
            chat_id = update.message.chat.id,
            text="**😔 360P QUALITY IS NOT AVAILABLE \n CHOOSE ANY OTHER QUALITIES**")  

    elif update.data == 'audio':
        await  HB.send_audio(
        chat_id = update.message.chat.id,
        audio=f"{str(yt.title)}.mp3",
        caption=result_text,
        duration=yt.length,
        progress=progress_for_pyrogram,
                    progress_args=(
                        UPLOAD_START,
                        update.message,
                        start_time
                    )
      )
        await update.message.delete()

    elif update.data == 'thumbnail':
        await HB.send_photo(
            chat_id = update.message.chat.id, 
            photo=thumb
        )
        await update.message.delete()    

    elif update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True
        )
    
    else:
        await update.message.delete()
import pytube
import re
from pytube import YouTube
from pytube import Playlist

@HB.on_message(filters.text & filters.private)
async def ytdl(_, update):
   purl=update.text
   pyt = Playlist(purl)
  
   for video in pyt.videos:
    phd =video.streams.get_highest_resolution()
    
    await  HB.send_video(
            chat_id = update.chat.id, 
            caption=(f"⭕️ PLAYLIST : "+ pyt.title + "\n" + video.title + "\n📥 DOWNLOADED " ),
            video = phd.download(),
            
        )
print("HB")
HB.run()
