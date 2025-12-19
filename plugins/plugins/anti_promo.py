from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
import re

PROMO_PATTERN = re.compile(
    r"(t\.me|telegram\.me|http://|https://|www\.|@[\w_]+)",
    re.IGNORECASE
)

@Client.on_message(
    filters.incoming &
    (filters.group | filters.private) &
    (
        filters.forwarded |
        filters.regex(PROMO_PATTERN)
    )
)
async def anti_promo_handler(client: Client, message: Message):

    # Allow admins in groups
    if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
        try:
            member = await client.get_chat_member(
                message.chat.id,
                message.from_user.id
            )
            if member.status in ("administrator", "creator"):
                return
        except:
            pass

    # Delete forwarded messages
    if message.forward_date:
        await message.delete()
        return

    # Delete promo text
    text = message.text or message.caption or ""
    if PROMO_PATTERN.search(text):
        await message.delete()
        return
