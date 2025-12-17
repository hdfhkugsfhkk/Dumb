from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatMemberStatus
import re

USERNAME_REGEX = r"@\w+"
TG_LINK_REGEX = r"(t\.me|telegram\.me)/\S+"

@Client.on_message(filters.all, group=0)
async def anti_promo_handler(client: Client, message: Message):

    if not message.from_user:
        return

    # Ignore bot itself
    if message.from_user.is_bot:
        return

    # Allow admins in groups
    if message.chat.type != ChatType.PRIVATE:
        try:
            member = await client.get_chat_member(
                message.chat.id, message.from_user.id
            )
            if member.status in (
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER
            ):
                return
        except:
            pass

    text = message.text or message.caption or ""

    # 1️⃣ Forwarded messages
    if message.forward_from or message.forward_from_chat:
        try:
            await message.delete()
        except:
            pass
        return

    # 2️⃣ Username (@someone)
    if re.search(USERNAME_REGEX, text):
        try:
            await message.delete()
        except:
            pass
        return

    # 3️⃣ Telegram links
    if re.search(TG_LINK_REGEX, text):
        try:
            await message.delete()
        except:
            pass
        return
