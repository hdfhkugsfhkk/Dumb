from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
import re

LINK_REGEX = r"(https?://|t\.me/|telegram\.me/|@[\w_]+)"

@Client.on_message(
    filters.group &
    (
        filters.regex(LINK_REGEX) |
        filters.forwarded
    )
)
async def anti_promo(client, message):

    if not message.from_user:
        return

    # Admin ignore
    try:
        member = await client.get_chat_member(
            message.chat.id,
            message.from_user.id
        )
        if member.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            return
    except:
        return

    try:
        await message.delete()
    except:
        pass

    await message.reply_text(
        "⚠️ **Links / forwarded messages not allowed**\n"
        "Grpil mathram movie request cheyyuka 🎬",
        quote=True
    )
