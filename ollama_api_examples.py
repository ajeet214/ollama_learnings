import ollama

# 🧠 List all available models installed locally
# print(ollama.list())

# 🔍 Show detailed info about a specific model (e.g., system prompt, template)
# print(ollama.show('llama3.2'))

# ⚙️ Create a new custom model based on an existing one, with a modified system prompt
# ollama.create(model='llama3.2_python', from_='llama3.2', system="You are Python and AI Expert.")

# ❌ Delete a local custom model
# ollama.delete('llama3.2_python')

# ⬇️ Pull a model from the Ollama registry (downloads it locally)
# ollama.pull('llama3.2')

# 📤 Push a local model to the Ollama registry (requires login and permissions)
# ollama.push('user/llama3.2')

# 📄 Copy a model locally under a different name
# ollama.copy('llama3.2', 'user/llama3.2')

# 🔡 Get embeddings (vector representations) for a single string
# print(ollama.embed(model='llama3.2', input='The sky is blue because of rayleigh scattering'))

# 🧬 Get embeddings for multiple strings at once
# print(ollama.embed(model='llama3.2', input=[
#     'The sky is blue because of rayleigh scattering',
#     'Grass is green because of chlorophyll'
# ]))

# 🚀 Show current model processes running (like server status)
# print(ollama.ps())

# 💬 Run a chat interaction using a list of messages (chat format)
# print(ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}]))

# ✍️ Generate a response from a single prompt (completion style)
# print(ollama.generate(model='llama3.2', prompt='Why is the sky blue?'))
