import os
import requests
import subprocess
from vars import OWNER, CREDIT, AUTH_USERS, TOTAL_USERS
from pyrogram import Client, filters
from pyrogram.types import Message

def register_authorisation_handlers(bot):
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_message(filters.command("addauth") & filters.private)
    async def add_auth_user(client: Client, message: Message):
        if message.chat.id != OWNER:
            return 
        try:
            new_user_id = int(message.command[1])
            if new_user_id in AUTH_USERS:
                await message.reply_text("**User ID is already authorized.**")
            else:
                AUTH_USERS.append(new_user_id)
                await message.reply_text(f"**User ID `{new_user_id}` added to authorized users.**")
                await client.send_message(chat_id=new_user_id, text=f"<b>🎉 Welcome to DRM Level 1 Bot! 🎉

You can have access to download all Non-DRM+AES Encrypted URLs 🔐 including:

   • 📚 Appx Zip+Encrypted Url
   • 🎓 Classplus DRM+ NDRM
   • 🧑‍🏫 PhysicsWallah DRM
   • 📚 CareerWill + PDF
   • 🎓 Khan GS
   • 🎓 Study Iq DRM
   • 🚀 APPX + APPX Enc PDF
   • 🎓 Vimeo Protection
   • 🎓 Brightcove Protection
   • 🎓 Visionias Protection
   • 🎓 Zoom Video
   • 🎓 Utkarsh Protection(Video + PDF)
   • 🎓 All Non DRM+AES Encrypted URLs
   • 🎓 MPD URLs if the key is known (e.g., Mpd_url?key=key XX:XX)


🚀 You are not subscribed to any plan yet!

💵 Monthly Plan: ₹ 1200
If you want to buy membership of the bot, feel free to contact the Bot Admin Naruto (0).</b>")
        except (IndexError, ValueError):
            await message.reply_text("**Please provide a valid user ID.**")
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_message(filters.command("users") & filters.private)
    async def list_auth_users(client: Client, message: Message):
        if message.chat.id != OWNER:
            return
    
        user_list = '\n'.join(map(str, AUTH_USERS))  # AUTH_USERS ki list dikhayenge
        await message.reply_text(f"**Authorized Users:**\n{user_list}")
  
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_message(filters.command("rmauth") & filters.private)
    async def remove_auth_user(client: Client, message: Message):
        if message.chat.id != OWNER:
            return
    
        try:
            user_id_to_remove = int(message.command[1])
            if user_id_to_remove not in AUTH_USERS:
                await message.reply_text("**User ID is not in the authorized users list.**")
            else:
                AUTH_USERS.remove(user_id_to_remove)
                await message.reply_text(f"**User ID `{user_id_to_remove}` removed from authorized users.**")
                await client.send_message(chat_id=user_id_to_remove, text=f"<b>Oops! You are removed from Premium Membership!</b>")
        except (IndexError, ValueError):
            await message.reply_text("**Please provide a valid user ID.**")
          
