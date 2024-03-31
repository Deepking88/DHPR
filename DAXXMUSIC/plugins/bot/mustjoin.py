import random 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from DAXXMUSIC import app

MISHI = [
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

#--------------------------

MUST_JOIN = "exampurrs"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(random.choice(MISHI), caption=f"❅ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !\n\n❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ʜᴇᴇʀ ᴍᴜꜱɪᴄ ʙᴏᴛ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʏᴏᴜ ᴊᴏɪɴᴇᴅ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/FONT_CHANNEL_01"),
                                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_ᴊᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
