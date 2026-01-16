from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest, Message
from info import REQ_CHANNEL1, REQ_CHANNEL2, ADMINS
from database.users_chats_db import db
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("jsyd"))
async def jreeq_menu(_, message):
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("❌ Remove Channel from All Users", callback_data="jsyd:remove")],
        [InlineKeyboardButton("❌ Delete ALL Join-Requests", callback_data="jsyd:del_all")],
        [InlineKeyboardButton("📊 View Count", callback_data="jsyd:count")],
        [InlineKeyboardButton("➕ Add Channel", callback_data="jsyd:add")],
        [InlineKeyboardButton("🗑 Remove One", callback_data="jsyd:remove_one")],
        [InlineKeyboardButton("❌ Clear All", callback_data="jsyd:clear")],
        [InlineKeyboardButton("📄 View List", callback_data="jsyd:view")],
        [InlineKeyboardButton("✖ Close", callback_data="jsyd:close")]
    ])

    await message.reply(
        "**📂 Join-Request Manager**\nSelect an option:",
        reply_markup=btn
    )




@Client.on_chat_join_request(filters.chat(REQ_CHANNEL1) | filters.chat(REQ_CHANNEL2))
async def join_reqs(b, join_req: ChatJoinRequest):
    user_id = join_req.from_user.id
    try:
        if join_req.chat.id == REQ_CHANNEL1:
            if join_req.invite_link.creator.id == b.me.id:
                await db.add_req_one(user_id)
        if join_req.chat.id == REQ_CHANNEL2:
            if join_req.invite_link.creator.id == b.me.id:
                await db.add_req_two(user_id)
    except Exception as e:
        print(f"Error adding join request: {e}")
        
@Client.on_callback_query(filters.regex("^jsyd:") & filters.user(ADMINS))
async def jsyd_callback(client, cb):
    d = cb.data.split(":", 1)[1]
    await cb.answer()
    if d == "remove":
        ask = await cb.message.reply("📨 Send the **channel ID** you want to remove from all users.")
        try:
            r = await client.listen(cb.from_user.id, timeout=60)
            if not r.text.isdigit():
                return await r.reply("❌ Invalid ID. Only numbers allowed.")
            cid = int(r.text)
            m = await db.remove_channel_from_all_users(cid)
            return await r.reply(f"✅ Removed `{cid}` from **{m}** users.")
        except TimeoutError:
            return await ask.edit("⏳ Timed out. Try again.")
    if d == "del_all":
        await db.del_all_join_req()
        return await cb.message.reply("🗑️ All join-requests deleted.")
    if d == "count":
        return await cb.message.reply(
            f"📊 Total join-requests: `{await db.req.count_documents({})}`"
        )
    if d == "close":
        return await cb.message.delete()
    if d == "view":
        ch = await db.get_fsub_list()
        return (
            await cb.answer("No force-sub channels set", show_alert=True)
            if not ch else
            await cb.message.edit_text(
                "📄 **Force-Sub Channels:**\n\n" + "\n".join(f"`{x}`" for x in ch)
            )
        )
    if d == "clear":
        await db.clear_fsub()
        await db.del_all_join_req()
        return await cb.message.edit_text("✅ Force-sub list cleared.")
    if d == "add":
        await cb.message.edit_text(
            "➕ **Send channel ID or forward a channel message**\n\nUse /cancel to abort."
        )
        try:
            m = await client.listen(cb.from_user.id, timeout=120)
            if m.text and m.text.lower() == "/cancel":
                return await cb.message.edit_text("❌ Cancelled.")
            cid = m.forward_from_chat.id if m.forward_from_chat else int(m.text.strip())
            await db.add_fsub_channel(cid)
            return await cb.message.edit_text(f"✅ Added `{cid}` to force-sub list.")
        except:
            return await cb.message.edit_text("❌ Invalid channel ID or timeout.")
    if d == "remove_one":
        ch = await db.get_fsub_list()
        if not ch:
            return await cb.answer("List is empty", show_alert=True)
        btn = [[InlineKeyboardButton(str(x), f"jsyd:del_{x}")] for x in ch]
        btn.append([InlineKeyboardButton("⬅ Back", "jsyd:menu")])
        return await cb.message.edit_text(
            "🗑 **Select channel to remove**",
            reply_markup=InlineKeyboardMarkup(btn)
        )
    if d.startswith("del_"):
        cid = int(d.split("_", 1)[1])
        await db.remove_fsub_channel(cid)
        m = await db.remove_channel_from_all_users(cid)
        return await cb.message.edit_text(f"✅ Removed `{cid}`, `{m}` from force-sub list.")
    if d == "menu":
        return await send_jsyd_menu(cb.message)
        
