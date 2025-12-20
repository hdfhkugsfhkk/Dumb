from pyrogram import Client, filters
from asyncio import sleep

WARNING_TEXT = (
    "⚠️ Warning!\n\n"
    "🔗 Links / usernames / forwarded messages are not allowed in this group.\n"
    "🎬 Please send only movie requests."
)

@Client.on_message(filters.group)
async def anti_promo_group_only(client, message):

    # Ignore service messages
    if not message.from_user:
        return

    user_id = message.from_user.id

    # ✅ Skip ADMINS / OWNER
    if user_id in ADMINS:
        return

    text = message.text or message.caption or ""

    # ❌ Check forward
    is_bad = bool(message.forward_date)

    # ❌ Check links / usernames
    if not is_bad:
        if (
            "http://" in text or
            "https://" in text or
            "t.me/" in text or
            text.startswith("@")
        ):
            is_bad = True

    if not is_bad:
        return  # ✅ Normal movie request → auto-filter continues

    try:
        # ⚠️ SEND WARNING FIRST
        warn = await client.send_message(
            chat_id=message.chat.id,
            text=WARNING_TEXT
        )

        # 🧹 Auto delete warning
        await sleep(8)
        await warn.delete()

        # ❌ NOW delete user message
        await message.delete()

    except:
        pass
