import chainlit as cl
from langroid.agent.callbacks.chainlit import add_instructions
from langroid import ChainlitTaskCallbacks
from core import setup_tasks

import nest_asyncio
nest_asyncio.apply()

MODEL = "groq/llama3-8b-8192"
@cl.on_chat_start
async def main():

    await add_instructions(
        title="Simple Search Assistant",
        content="Welcome to the Web Search Assistant! I will try to answer your complex questions."
    )

    assistant_task = setup_tasks()
    cl.user_session.set("assistant_task", assistant_task)


@cl.on_message
async def on_message(message: cl.Message):
    assistant_task = cl.user_session.get("assistant_task")
    ChainlitTaskCallbacks(assistant_task, message)
    await assistant_task.run_async(message.content)