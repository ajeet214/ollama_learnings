import asyncio
from ollama import AsyncClient


async def chat():

    """Stream and print response parts asynchronously from an Ollama model."""
    message = {'role': 'user', 'content': 'Why is the sky blue?'}

    async for part in await AsyncClient().chat(model='llama3.2', messages=[message], stream=True):
        print(part['message']['content'], end='', flush=True)


if __name__ == "__main__":
    asyncio.run(chat())
