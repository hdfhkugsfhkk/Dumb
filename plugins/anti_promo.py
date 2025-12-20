from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
import re
from info import LOG_CHANNEL

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

    # Ignore admins
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

    user = message.from_user
    chat = message.chat
    text = message.text or message.caption or "❌ No text"

    reason = "Forwarded Message" if message.forward_date else "Link / Username"

    # Delete message
    try:
        await message.delete()
    except:
        pass

    # Warning in group
    await message.reply_text(
        "⚠️ **Links / forwarded messages not allowed**\n"
        "Grpil mathram movie request cheyyuka 🎬",
        quote=True
    )

    # Log to channel
    log_text = (
        "🚫 **Message Deleted**\n\n"
        f"👤 **User:** {user.mention} (`{user.id}`)\n"
        f"👥 **Group:** {chat.title}\n"
        f"🆔 **Group ID:** `{chat.id}`\n"
        f"📌 **Reason:** {reason}\n\n"
        f"📝 **Message:**\n{text}"
    )

    try:
        await client.send_message(LOG_CHANNEL, log_text)
    except:
        pass
