import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from DAXXMUSIC import app  

ABHI = [
"https://telegra.ph/file/f350818b3b267280ebb7b.jpg",
"https://telegra.ph/file/6f656beef0b24b1082136.jpg",
"https://telegra.ph/file/2dc5d2c417fae288275a0.jpg",
"https://telegra.ph/file/0462eacbef102ae6f0d80.jpg",
"https://telegra.ph/file/1231e8086b4bcbca8a12b.jpg",
"https://telegra.ph/file/646053f894fde8da84a87.jpg",
"https://telegra.ph/file/b11f82a48e0920f7ebcb7.jpg",
"https://telegra.ph/file/4e94c837043ea4e8b0de0.jpg",
"https://telegra.ph/file/d4b82210a6c2aa6f5c327.jpg",
"https://telegra.ph/file/29e4629051b5159a0edde.jpg",
"https://telegra.ph/file/303ea976ff9594b61c419.jpg",
"https://telegra.ph/file/29e4629051b5159a0edde.jpg",
"https://telegra.ph/file/0462eacbef102ae6f0d80.jpg",
"https://telegra.ph/file/0462eacbef102ae6f0d80.jpg",
"https://telegra.ph/file/d4b82210a6c2aa6f5c327.jpg",
"https://telegra.ph/file/d4b82210a6c2aa6f5c327.jpg",
"https://telegra.ph/file/4e94c837043ea4e8b0de0.jpg",
"https://telegra.ph/file/303ea976ff9594b61c419.jpg",
"https://telegra.ph/file/efc616221c814994eb36a.jpg",
"https://telegra.ph/file/657820a0d766b79cf71f9.jpg",
"https://telegra.ph/file/4cd6e74cb2e0ca6f721b5.jpg",
"https://telegra.ph/file/4cd6e74cb2e0ca6f721b5.jpg",
"https://telegra.ph/file/303ea976ff9594b61c419.jpg",
"https://telegra.ph/file/806cbf71b2a386934fc58.jpg",
"https://telegra.ph/file/646053f894fde8da84a87.jpg",
"https://telegra.ph/file/b11f82a48e0920f7ebcb7.jpg",
"https://telegra.ph/file/4e94c837043ea4e8b0de0.jpg",
"https://telegra.ph/file/d4b82210a6c2aa6f5c327.jpg",
"https://telegra.ph/file/29e4629051b5159a0edde.jpg",   

]

NYKAA = [
    "https://telegra.ph/file/efc616221c814994eb36a.jpg",
    "https://telegra.ph/file/806cbf71b2a386934fc58.jpg",
    "https://telegra.ph/file/657820a0d766b79cf71f9.jpg",
    "https://telegra.ph/file/4cd6e74cb2e0ca6f721b5.jpg",
    "https://telegra.ph/file/4cd6e74cb2e0ca6f721b5.jpg",
    "https://telegra.ph/file/806cbf71b2a386934fc58.jpg",
    "https://telegra.ph/file/dc5e914d1da95b4228084.jpg",
    "https://telegra.ph/file/646053f894fde8da84a87.jpg",
    "https://telegra.ph/file/4e94c837043ea4e8b0de0.jpg",
    "https://telegra.ph/file/b11f82a48e0920f7ebcb7.jpg",
    "https://telegra.ph/file/f350818b3b267280ebb7b.jpg",
    "https://telegra.ph/file/6f656beef0b24b1082136.jpg",
    "https://telegra.ph/file/2dc5d2c417fae288275a0.jpg",
    "https://telegra.ph/file/2dc5d2c417fae288275a0.jpg",
    "https://telegra.ph/file/0462eacbef102ae6f0d80.jpg",
    "https://telegra.ph/file/0462eacbef102ae6f0d80.jpg",
    "https://telegra.ph/file/0462eacbef102ae6f0d80.jpg",
    "https://telegra.ph/file/1231e8086b4bcbca8a12b.jpg",
    "https://telegra.ph/file/2dc5d2c417fae288275a0.jpg",
    "https://telegra.ph/file/6f656beef0b24b1082136.jpg",
    "https://telegra.ph/file/f350818b3b267280ebb7b.jpg",
    "https://telegra.ph/file/6f656beef0b24b1082136.jpg",
    "https://telegra.ph/file/2dc5d2c417fae288275a0.jpg",
    "https://telegra.ph/file/0462eacbef102ae6f0d80.jpg",
    "https://telegra.ph/file/1231e8086b4bcbca8a12b.jpg",
    "https://telegra.ph/file/4e94c837043ea4e8b0de0.jpg",
    "https://telegra.ph/file/b11f82a48e0920f7ebcb7.jpg",
    "https://telegra.ph/file/646053f894fde8da84a87.jpg",
    "https://telegra.ph/file/dc5e914d1da95b4228084.jpg",
    "https://telegra.ph/file/806cbf71b2a386934fc58.jpg",    
]



@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❀ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❀\n\n"
               
                f"๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {message.chat.title}\n"
                f"๏ ɢʀᴏᴜᴘ ɪᴅ ➠ {message.chat.id}\n"
                f"๏ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠ @{message.chat.username}\n"
                f"๏ ɢʀᴏᴜᴘ ʟɪɴᴋ ➠[ʙᴀʙʏ ᴛᴏᴜᴄʜ]({link})\n"
                f"๏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➠ {count}\n"
                f"๏ ᴀᴅᴅᴇᴅ ʙʏ ➠ {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(ABHI), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"❀ <b><u>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ʙʏ ᴀ ᴄʜᴜᴛɪʏᴀ</u></b> ❀\n\n๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {title}\n\n๏ ɢʀᴏᴜᴘ ɪᴅ ➠ {chat_id}\n\n๏ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➠ {remove_by}\n\n๏ ʙᴏᴛ ɴᴀᴍᴇ ➠ @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(NYKAA), caption=left, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❀ ʜᴇʏ {message.from_user.mention} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ❀\n\n"
                
                f"๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {message.chat.title}\n"
                f"๏ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠ @{message.chat.username}\n"
                f"๏ ʏᴏᴜʀ ɪᴅ ➠ {member.id}\n"
                f"๏ ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍᴇ ➠ @{member.username}\n"
                f"๏ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴏᴛᴇʟ {count} ᴍᴇᴍʙᴇʀs"
            )
            await app.send_photo(message.chat.id, photo=random.choice(NYKAA), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))


        
