from pyrogram import Client, filters
from asyncio import sleep

WARNING_TEXT = (
    "⚠️ Warning!\n\n"
    "🔗 Links / usernames / forwarded messages are not allowed in this group.\n"
    "🎬 Please send only movie requests."
)

BAD_PATTERN = r"(https?://|t\.me/|@\w+)"

@Client.on_message(
    filters.group &
    (filters.forwarded | filters.regex(BAD_PATTERN)),
    group=-1
)
async def anti_promo_group_only(client, message):

    if not message.from_user:
        return

    # ✅ Skip admins
    if message.from_user.id in ADMINS:
        return

    try:
        # ⚠️ Send warning
        warn = await client.send_message(
            chat_id=message.chat.id,
            text=WARNING_TEXT
        )

        await sleep(8)
        await warn.delete()

        # ❌ Delete bad message
        await message.delete()

    except:
        pass
