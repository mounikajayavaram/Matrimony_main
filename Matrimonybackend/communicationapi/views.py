# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@api_view(['POST'])
def send_message(request):
    message = request.data.get('message')

    # Validate the message content as needed

    # Get the channel layer
    channel_layer = get_channel_layer()

    # Send the message to the "chat" channel
    async_to_sync(channel_layer.group_send)(
        "chat",
        {
            "type": "chat.message",
            "message": message,
        },
    )

    return Response({"status": "ok"})
