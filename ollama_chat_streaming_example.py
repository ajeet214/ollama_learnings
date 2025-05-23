# Import the chat function and ChatResponse class from the ollama package
from ollama import chat
from ollama import ChatResponse

# Send a streaming chat request to the Ollama model 'llama3.2'
# 'stream=True' enables chunk-by-chunk streaming of the response
stream_response: ChatResponse = chat(
    model='llama3.2',  # Specify the model to use
    messages=[
        {
            'role': 'user',  # Indicates the speaker; 'user' is the person prompting the model
            'content': 'Why is the sky blue?',  # The question or prompt sent to the model
        },
    ],
    stream=True  # Enables streaming of the response instead of waiting for full completion
)

# Iterate through the streamed response chunks as they arrive
for chunk in stream_response:
    # Each chunk contains part of the model's message
    # Print each chunk's content without a newline and flush output to display in real time
    print(chunk.message.content, end='', flush=True)
