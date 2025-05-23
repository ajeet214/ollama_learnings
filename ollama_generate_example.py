"""
This script demonstrates how to use the `generate()` function from the `ollama` Python package.

Function signature:

generate(
    model='llama3.2',                     # Name of the model to use
    prompt='',                            # The input prompt text (the prompt to generate a response for)
    suffix='',                            # text appended after the model's response
    images='',                            # (optional) a list of Base64-encoded images (used for multimodal models like llava)
    format='',                            # The format to return a response in. Format can be json or a JSON schema.
    options={                             # Optional generation parameters
        'temperature': float,             # The temperature of the model. Increasing the temperature will make the model answer more creatively. (Default: 0.8)
        'seed': int,                      # Sets the random number seed to use for generation. Setting this to a specific number will make the model generate the same text for the same prompt. (Default: 0)
        'num_predict': int,               # Maximum number of tokens to predict when generating text. (Default: -1, infinite generation)
        'top_k': int,                     # Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)
        'top_p': float                    # Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)
    },
    system='',                            # System message to (overrides what is defined in the Modelfile) (optional)
    template='',                          # The prompt template to use (overrides what is defined in the Modelfile) (optional)
    stream=False,                         # If True, returns streamed chunks instead of full response
    keep_alive='5m'                       # How long the model should stay in memory after use
)
"""
# Import the generate function and GenerateResponse class from the ollama package
from ollama import generate
from ollama import GenerateResponse

# Send a generate request to the Ollama model (in this case, 'llama3.2') with a prompt
response: GenerateResponse = generate(
  model='llama3.2',
  prompt='Act as a Python expert and write a code to add two numbers.',

)

# Print the model's response using attribute-style access (recommended)
print(response.response)
