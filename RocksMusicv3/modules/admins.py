# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit

from asyncio import QueueEmpty
from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import Message

from RocksMusicv3.config import que
from RocksMusicv3.function.admins import set
from RocksMusicv3.helpers.channelmusic import get_chat_id
from RocksMusicv3.helpers.decorators import authorized_users_only
from RocksMusicv3.helpers.decorators import errors
from RocksMusicv3.helpers.filters import command
from RocksMusicv3.helpers.filters import other_filters
from RocksMusicv3.services.callsmusic import callsmusic
from RocksMusicv3.services.queues import queues


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Aᴅᴍɪɴ ᴄʜᴀᴄᴇ Rᴇғʀᴇsʜᴇᴅ!")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.active_chats) or (
        callsmusic.active_chats[chat_id] == "paused"
    ):
        await message.reply_text("❗ Nᴏᴛʜɪɴɢ ɪs Pʟᴀʏɪɴɢ...☺️!")
    else:
        callsmusic.pause(chat_id)
        await message.reply_text("▶️ Pᴀᴜsᴇᴅ...😜!")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.active_chats) or (
        callsmusic.active_chats[chat_id] == "playing"
    ):
        await message.reply_text("❗ Nᴏᴛʜɪɴɢ ɪs Pᴀᴜsᴇᴅ...😔!")
    else:
        callsmusic.resume(chat_id)
        await message.reply_text("⏸ Rᴇsᴜᴍᴇᴅ...🥺!")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ Nᴏᴛʜɪɴɢ ɪs Sᴛʀᴇᴀᴍɪɴɢ...🤗!")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass

        await callsmusic.stop(chat_id)
        await message.reply_text("❌ Mᴜsɪᴄ Eɴᴅᴇᴅ...!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ Pᴇʜʟᴇʏ Sᴏɴɢ Pʟᴀʏ Kᴇʀ Lᴏ Nɪᴋᴀᴍᴇʏ...👉!")
    else:
        queues.task_done(chat_id)
        if queues.is_empty(chat_id):
            await callsmusic.stop(chat_id)
        else:
            await callsmusic.set_stream(
                chat_id, 
                queues.get(chat_id)["file_path"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"- Sᴋɪᴘᴘᴇᴅ...😉 **{skip[0]}**\n- Nᴏᴡ Pʟᴀʏɪɴɢ...👉 **{qeue[0][0]}**")


@Client.on_message(filters.command("admincache"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Aᴅᴍɪɴ ᴄᴀᴄʜᴇ Rᴇғʀᴇsʜᴇᴅ...!")
