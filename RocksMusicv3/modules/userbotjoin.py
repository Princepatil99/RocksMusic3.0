
from pyrogram import Client
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from RocksMusicv3.helpers.decorators import authorized_users_only
from RocksMusicv3.helpers.decorators import errors
from RocksMusicv3.services.callsmusic import client as USER
from RocksMusicv3.config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>𝐀𝐝𝐝 𝐦𝐞 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧 𝐨𝐟 𝐲𝐨𝐫 𝐠𝐫𝐨𝐮𝐩 𝐟𝐢𝐫𝐬𝐭</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "RocksMusicv3"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "**Jᴜsᴛ ᴄʜɪʟʟ ʙʀᴏ ᴍᴀɪɴ ʏᴀʜᴀɴ ᴍᴜsɪᴄ ᴘʟᴀʏ ᴋᴀʀɴᴇʏ ᴀʏᴀ ʜᴏɴ...💗**")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>**Kᴀɴ ᴋʏ ɴᴇᴇᴄʜᴇʏ ᴅᴏ ʟᴀɢᴀᴏɴ ᴍᴀɪɴ ʏᴀʜᴀɴ ᴘᴇʜʟᴇʏ sᴇʏ ʜᴏɴ**😉</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 𝐅𝐥𝐨𝐨𝐝 𝐖𝐚𝐢𝐭 𝐄𝐫𝐫𝐨𝐫 🛑 \n User {user.first_name} 𝐜𝐨𝐮𝐥𝐝𝐧'𝐭 𝐣𝐨𝐢𝐧 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 𝐝𝐮𝐞 𝐭𝐨 𝐡𝐞𝐚𝐯𝐲 𝐣𝐨𝐢𝐧 𝐫𝐞𝐪𝐮𝐞𝐬𝐭𝐬 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫𝐛𝐨𝐭! 𝐌𝐚𝐤𝐞 𝐬𝐮𝐫𝐞 𝐮𝐬𝐞𝐫 𝐢𝐬 𝐧𝐨𝐭 𝐛𝐚𝐧𝐧𝐞𝐝 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩. **Or To Contact @Dr_Asad_Ali**"
            "\n\nOr 𝐦𝐚𝐧𝐮𝐚𝐥𝐥𝐲 𝐚𝐝𝐝 𝐌𝐲 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧</b>",
        )
        return
    await message.reply_text(
        "<b>**Mᴀɪɴ ᴀᴀ Gᴀʏᴀ**😜</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>𝐔𝐬𝐞𝐫 𝐜𝐨𝐮𝐥𝐝𝐧'𝐭 𝐥𝐞𝐚𝐯𝐞 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩! 𝐌𝐚𝐲 𝐛𝐞 𝐟𝐥𝐨𝐨𝐝𝐰𝐚𝐢𝐭𝐬."
            "\n\nOr 𝐦𝐚𝐧𝐮𝐚𝐥𝐥𝐲 𝐤𝐢𝐜𝐤 𝐦𝐞 𝐟𝐫𝐨𝐦 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐋𝐞𝐚𝐯𝐢𝐧𝐠 𝐚𝐥𝐥 𝐜𝐡𝐚𝐭𝐬")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐋𝐞𝐚𝐯𝐢𝐧𝐠... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐋𝐞𝐚𝐯𝐢𝐧𝐠... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("𝐈𝐬 𝐜𝐡𝐚𝐭 𝐞𝐯𝐞𝐧 𝐥𝐢𝐧𝐤𝐞𝐝")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>𝐀𝐝𝐝 𝐦𝐞 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧 𝐨𝐟 𝐲𝐨𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐟𝐢𝐫𝐬𝐭</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "RocksMusicv3"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "𝐈 𝐣𝐨𝐢𝐧𝐞𝐝 𝐡𝐞𝐫𝐞 𝐚𝐬 𝐲𝐨𝐮 𝐫𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>🅡︎🅞︎🅒︎🅚︎🅢︎ 𝐡𝐞𝐥𝐩𝐞𝐫 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐣𝐨𝐢𝐧𝐞𝐝 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 𝑭𝒍𝒐𝒐𝒅 𝑾𝒂𝒊𝒕 𝑬𝒓𝒓𝒐𝒓 🛑 \n User {user.first_name} couldn't join your channel due to heavy join requests for userbot! Make sure user is not banned in channel, or contact to @Dr_Asad_Ali"
            "\n\nOr 𝐦𝐚𝐧𝐮𝐚𝐥𝐥𝐲 𝐚𝐝𝐝 𝐌𝐲 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧</b>",
        )
        return
    await message.reply_text(
        "<b>🅡︎🅞︎🅒︎🅚︎🅢︎ 𝐡𝐞𝐥𝐩𝐞𝐫 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐣𝐨𝐢𝐧𝐞𝐝 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥</b>",
    )
    
