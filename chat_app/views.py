from django.shortcuts import render

# Create your views here.
from chat_app.models import Message
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def chat_list(request):
    chats= Message.objects.all().order_by('timestamp')
    return render(
        request,
        "chat_list.html",
        {"chats":chats,
        "now": timezone.now(),          
        "TIME_ZONE": timezone.get_current_timezone_name()}
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
        return redirect("chat-list")   
    

    messages = Message.objects.all().order_by("timestamp")
    return render(
        request,
        "chat_list.html", 
        {"chats": messages})

    