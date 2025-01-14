import ollama

def generate_response(messages):
    model='llama3'
    LastMessage = messages[-1]
    if 'llava' in LastMessage['content'].lower():
        model='llava'
    response = ollama.chat(
        model='llama3',
        messages=messages,
        stream=False,
    )
    return response
