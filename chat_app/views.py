from django.shortcuts import render

# Create your views here.
from chat_app.models import Message


def chat_list(request):
    chats= Message.objects.all()
    return render(
        request,
        "chat_list.html",
        {"chats":chats}
    )