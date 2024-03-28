from telegraph import upload_file
from pyrogram import filters
from DAXXMUSIC import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tgm" , "tm"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("๏ ᴍᴀᴋᴇ ᴀ ʟɪɴᴋ...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'๏ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴘʜ ᴜʀʟ ɪs ʀᴇᴀᴅʏ ʙᴀʙʏ ➠ {url}\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ [˹𝙳𝙷𝙿𝚁˼](https://t.me/FONT_CHANNEL_01)')

########____________________________________________________________######

@app.on_message(filters.command(["graph" , "grf"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("๏ ᴍᴀᴋᴇ ᴀ ʟɪɴᴋ...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x

        i.edit(f'๏ ʏᴏᴜʀ ɢʀᴀᴘʜ ᴜʀʟ ɪs ʀᴇᴀᴅʏ ʙᴀʙʏ ➠ {url}\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ [˹𝙳𝙷𝙿𝚁˼](https://t.me/FONT_CHANNEL_01)')

