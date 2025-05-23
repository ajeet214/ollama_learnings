"""
--------------------
Demonstrates how to send a single prompt to an Ollama model **asynchronously**
using `AsyncClient`, then print the model’s reply.

If your Ollama server is remote or secured, pass `host=` and `headers=` when
creating `AsyncClient(host="https://ollama.yourdomain.com", headers=...)`.
"""

import asyncio
from ollama import AsyncClient, ChatResponse


async def chat() -> None:
    """Send a message asynchronously to the Ollama model and print the response."""
    message = {"role": "user", "content": "Why is the sky blue?"}

    # Instantiate the AsyncClient (no context manager needed)
    client = AsyncClient()

    # Send the message to the model
    response: ChatResponse = await client.chat(model="llama3.2", messages=[message])

    # Print the assistant's reply
    print(response.message.content)


if __name__ == "__main__":
    asyncio.run(chat())
