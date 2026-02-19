from django.urls import path

from chat_app import views

urlpatterns = [
    path("", views.chat_list, name="chat-list"),
    path('send/', views.send_message, name="send-message"),
]