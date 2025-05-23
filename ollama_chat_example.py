""""
This script demonstrates how to use the `chat()` function from the `ollama` Python package.

Function signature:

chat(
    # name of the model to use
    model='llama3.2',
    # the messages of the chat, this can be used to keep a chat memory
    messages=[
        {
            'role': ' the role of the message, either system, user, assistant, or tool',
            'content': 'the content of the message',
            'images': ' (optional): a list of images to include in the message (for multimodal models such as llava)',
            'tool_calls': ' (optional): a list of tools in JSON that the model wants to use'

        }
    ],
    # list of tools in JSON for the model to use if supported
    tools=[],
    #  the format to return a response in. Format can be json or a JSON schema.
    format='',
    options={
        # The temperature of the model. Increasing the temperature will make the model answer more creatively. (Default: 0.8)
        'temperature': float,
        # Sets the random number seed to use for generation. Setting this to a specific number will make the model generate the same text for the same prompt. (Default: 0)
        'seed': int,
        # Maximum number of tokens to predict when generating text. (Default: -1, infinite generation)
        'num_predict': -1,
        # Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)
        'top_k': int,
        # Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)
        'top_p': float
    },
    #  if false the response will be returned as a single response object, rather than a stream of objects
    stream=bool,
    # keep_alive: controls how long the model will stay loaded into memory following the request (default: 5m)
    keep_alive=5
)
"""
# Import the chat function and ChatResponse class from the ollama package
from ollama import chat
from ollama import ChatResponse

# Send a chat request to the Ollama model (in this case, 'llama3.2') with a user message
# The 'messages' parameter is a list of message dictionaries with 'role' and 'content'
response: ChatResponse = chat(
  model='llama3.2',
  messages=[
    {
        'role': 'user',  # Role indicates who is sending the message ('user', 'assistant', etc.)
        'content': 'Why is the sky blue?',  # The actual user input to the language model
    },
  ]
)

# Print the model's response using attribute-style access (recommended)
print(response.message.content)
