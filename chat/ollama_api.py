import ollama

def generate_response(messages):
    response = ollama.chat(
        model='llama3',
        messages=messages,
        stream=False,
    )
    return response
