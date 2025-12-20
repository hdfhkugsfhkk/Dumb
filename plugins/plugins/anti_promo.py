from pyrogram import Client, filters
from pyrogram.enums import ChatType
from asyncio import sleep

WARNING_TEXT = (
    "⚠️ **Warning!**\n\n"
    "🔗 Links / usernames / forwarded messages are not allowed in this group.\n"
    "🎬 Please send only movie requests."
)

@Client.on_message(filters.group)
async def anti_promo_group_only(client, message):

    # Ignore service msgs
    if not message.from_user:
        return

    user_id = message.from_user.id

    # ✅ Skip ADMINS / OWNER
    if user_id in ADMINS:
        return

    text = message.text or message.caption or ""

    delete_reason = False

    # ❌ Forwarded message
    if message.forward_date:
        delete_reason = True

    # ❌ Links / usernames
    elif (
        "http://" in text or
        "https://" in text or
        "t.me/" in text or
        text.startswith("@")
    ):
        delete_reason = True

    if delete_reason:
        try:
            await message.delete()

            warn = await client.send_message(
                chat_id=message.chat.id,
                text=WARNING_TEXT
            )

            # 🧹 Auto delete warning after 8 sec
            await sleep(8)
            await warn.delete()

        except:
            pass

        return  # 🚫 Stop here, auto-filter safe
