from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest, Message
from info import REQ_CHANNEL1, REQ_CHANNEL2, ADMINS
from database.users_chats_db import db

@Client.on_message(filters.command("jreq") & filters.user(ADMINS))
async def jreq_menu(_, message):
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("❌ Remove Channel from All Users", "jsyd:remove")],
        [InlineKeyboardButton("❌ Delete ALL Join-Requests", "jsyd:del_all")],
        [InlineKeyboardButton("📊 View Count", "jsyd:count")],
        [InlineKeyboardButton("➕ Add Channel", "jsyd:add")],
        [InlineKeyboardButton("🗑 Remove One", "jsyd:remove_one")],
        [InlineKeyboardButton("❌ Clear All", "jsyd:clear")],
        [InlineKeyboardButton("📄 View List", "jsyd:view")],
        [InlineKeyboardButton("✖ Close", "jsyd:close")]
    ])
    await message.reply("**📂 Join-Request Manager**\nSelect an option:", reply_markup=btn)

