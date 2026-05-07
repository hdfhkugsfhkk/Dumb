from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import ADMINS


@Client.on_message(filters.command("link") & filters.user([7425490417, 1509123054, 7579162275]))
async def generate_link(client, message):
    command_text = message.text.split(maxsplit=1)
    if len(command_text) < 2:
        await message.reply("Please provide the name for the movie! Example: /link game of thrones")
        return
    movie_name = command_text[1].replace(" ", "-")
    link = f"https://t.me/ChithramMovieBot?start=getfile-{movie_name}"
    
    await message.reply(
        text=f"Here is your link: {link}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url={link}")]]
        )
    )
    
FUB_TEXT ="""<b><blockquote>You can find the bot commands here.</blockquote>

‣ /logs - Get logs as a file

‣ /restart - Restart the bot

‣ /stats - Get bot user stats (Will send only after checking active users & Get count of total files in DB

‣ /broadcast - Reply to a message to send that to all bot users

‣ /deleteall - This will delete all indexed files.

‣ /settings - Group settings 

‣ /gfilter - Global filter Adding

‣ /viewgfilters - Total Global filter Show

‣ /delg - special Global filter Delete

‣ /delallg - All Global filter Delete

‣ /filter - adding Filter

‣ /filters - show all Filters

‣ /del - Global filter Delete

‣ /delall - All Filter Delete

‣ /deletefiles - special movie files delete

‣ /deletesmallfiles - 

‣ /delete_duplicate - 

‣ /link - Movie Link Carte

‣ /index - Start indexing a database channel (bot must be admin of the channel if that is private channel)
You can just forward the message from database channel for starting indexing, no need to use the /index command
/indexlink - Start indexing a database channel using link (bot must be admin of the channel if that is private channel)
/indexlink  or /indexlink  

‣ /delete - Reply to a file to delete it from database

‣ /setchat1 - <i>Set force subscribe channel - /setchat1 channel_id (Answer the questions after that) Bot must be admin of that channel (Bot will create a new invite link)</i>

‣ /setchat2 - <i>Set force subscribe channel - /setchat2 channel_id (Answer the questions after that) Bot must be admin of that channel (Bot will create a new invite link)</i>

‣ /delchat1 - <i>delete Force subscribe channel</i>

‣ /delchat2 - <i>delete Force subscribe channel</i>

‣ /viewchat1 - <i>Check invite link for force subscribe channel</i>

‣ /viewchat2 - <i>Check invite link for force subscribe channel</i>

‣ /purge_one - <i>Clear all force subscribe users from db</i>

‣ /purge_two - <i>Clear all force subscribe users from db</i>

‣ /totalreq - <i>Total all force subscribe Count</i></b>"""

@Client.on_message(filters.command("help") & filters.private & filters.user(ADMINS))
async def generate_link(client, message):
    command_text = message.text.split(maxsplit=1)
    if len(command_text) < 2:
        await message.reply(FUB_TEXT)
        return
