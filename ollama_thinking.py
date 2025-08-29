from ollama import chat


def ask_question(model_name: str, question: str, enable_thinking: bool = True):
    """
    Ask a question using Ollama's chat interface.

    Args:
        model_name (str): The name of the model (e.g., 'deepseek-r1').
        question (str): The user's question.
        enable_thinking (bool): Whether to show the model's reasoning process.

    Returns:
        tuple: (thinking string, response string)
    """
    messages = [{'role': 'user', 'content': question}]

    response = chat(model_name, messages=messages, think=enable_thinking)
    thinking = response.message.thinking if enable_thinking else "Thinking disabled."
    answer = response.message.content

    return thinking, answer


# === Usage Example ===
if __name__ == "__main__":
    model = "llama3.2"
    question = "What is 10 + 23?"

    thinking, answer = ask_question(model, question)

    print("Thinking:\n========\n" + thinking)
    print("\nResponse:\n========\n" + answer)
