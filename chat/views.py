from django.shortcuts import render
from django.http import StreamingHttpResponse
from .ollama_api import generate_response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

messages = []
systemmessage = {
    "role": "system",
    "content": "You are a goth. You are into all things dark and macabre",
}
messages.append(systemmessage)

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        user_input = request.POST["user_input"]
        messages.append({
            "role": "user",
            "content": user_input
        })
        response = generate_response(messages)
        #print(response['message']['content'])
        formatted_response = response['message']['content']
        print(formatted_response)
        messages.append({
            "role": "assistant",
            "content": formatted_response
        })
        return StreamingHttpResponse(formatted_response, content_type='text/plain')
    return render(request, "chat.html")