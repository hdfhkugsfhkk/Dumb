from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
import re

LINK_REGEX = r"(https?://|t\.me/|telegram\.me/|@[\w_]+)"

@Client.on_message(filters.group & (filters.text | filters.caption))
async def anti_promo(client, message):

    # Ignore service messages
    if not message.from_user:
        return

    # Admin check
    try:
        member = await client.get_chat_member(message.chat.id, message.from_user.id)
        if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            return
    except:
        return

    text = message.text or message.caption or ""

    # Forwarded message check
    if message.forward_date:
        await message.delete()
        await message.reply_text(
            "⚠️ **Forwarded messages are not allowed here.**\n"
            "Grpil mathram message ayakkanam 🙂",
            quote=True
        )
        return

    # Link / username check
    if re.search(LINK_REGEX, text.lower()):
        await message.delete()
        await message.reply_text(
            "⚠️ **Links & usernames are not allowed!**\n"
            "Grpil matram movie request cheyyuka 🎬",
            quote=True
        )
        return

    # ❗ VERY IMPORTANT
    # Do NOT return here
    # Let auto filter continue
