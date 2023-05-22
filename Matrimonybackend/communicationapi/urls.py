from django.urls import path
from . import views

urlpatterns = [
    # ... your other URL patterns here ...
    path('send-message/', views.send_message, name='send_message'),
]
