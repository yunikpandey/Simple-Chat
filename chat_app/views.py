from django.shortcuts import render

# Create your views here.
from chat_app.models import Message
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def chat_list(request):
    chats= Message.objects.all()
    return render(
        request,
        "chat_list.html",
        {"chats":chats}
    )


@login_required
def send_message(request):
    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        if content:
            Message.objects.create(
                sender=request.user,
                content=content
            )
        return redirect("chat-list")   # or "chat-list" — use the name you defined

    # If someone tries GET → just redirect
    return redirect("chat-list")