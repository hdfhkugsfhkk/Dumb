from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
import re

# Link & username pattern
LINK_PATTERN = re.compile(
    r"(t\.me|telegram\.me|http://|https://|www\.|@[\w_]+)",
    re.IGNORECASE
)

@Client.on_message(
    filters.incoming &
    (filters.group | filters.private)
)
async def anti_promo_handler(client: Client, message: Message):

    # Skip service messages
    if not message.text and not message.caption and not message.forward_date:
        return

    # Allow admins in groups
    if message.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
        try:
            member = await client.get_chat_member(message.chat.id, message.from_user.id)
            if member.status in ("administrator", "creator"):
                return
        except:
            pass

    # ❌ Delete forwarded messages
    if message.forward_date:
        try:
            await message.delete()
        except:
            pass
        return

    text = message.text or message.caption or ""

    # ❌ Delete links / usernames
    if LINK_PATTERN.search(text):
        try:
            await message.delete()
        except:
            pass
        return
