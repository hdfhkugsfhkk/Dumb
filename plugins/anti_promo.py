from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType

import re

USERNAME_REGEX = r"@\w+"
TG_LINK_REGEX = r"(https?://)?(t\.me|telegram\.me)/\S+"

@Client.on_message(
    filters.group | filters.private,
    group=5
)
async def anti_promo(client: Client, message: Message):

    # Ignore bot messages
    if message.from_user and message.from_user.is_bot:
        return

    # OPTIONAL: Allow admins
    if message.chat.type != ChatType.PRIVATE:
        try:
            member = await client.get_chat_member(
                message.chat.id, message.from_user.id
            )
            if member.status in ("administrator", "owner"):
                return
        except:
            pass

    text = message.text or message.caption or ""

    # Check forwarded messages
    if message.forward_from or message.forward_from_chat:
        await message.delete()
        return

    # Check @username
    if re.search(USERNAME_REGEX, text):
        await message.delete()
        return

    # Check telegram links
    if re.search(TG_LINK_REGEX, text):
        await message.delete()
        return
