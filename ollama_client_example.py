"""
✅ Key Points:
- Client allows setting persistent configuration like host and headers.
- Useful if you're interacting with a self-hosted Ollama server (e.g., in a Docker container or on another machine).
"""

# Import the Client class from the ollama package
from ollama import Client
from ollama import ChatResponse

# Create a Client instance to interact with a locally hosted Ollama server
client = Client(
    host='http://localhost:11434',  # URL of the Ollama server (default localhost)
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}  # Optional custom headers, e.g., for auth or tracking
)

# Send a chat request using the specified model and a single user message
response: ChatResponse = client.chat(
    model='llama3.2',  # The name of the Ollama model to use (e.g., 'llama3.2')
    messages=[
        {
            'role': 'user',  # Indicates the role in the conversation: 'user', 'assistant', etc.
            'content': 'Why is the sky blue?',  # The actual question or prompt
        },
    ]
)

# Print the model's response using attribute-style access
print(response.message.content)

