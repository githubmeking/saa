from pyrogram import Client
from pytgcalls import PyTgCalls
import config
from . import queues

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)

@pytgcalls.on_closed_voice_chat()
async def on_closed(chat_id: int) -> None:
    queues.task_done(chat_id)
    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.change_stream(
            chat_id, queues.get(chat_id)["file"]
        )

run = pytgcalls.run
