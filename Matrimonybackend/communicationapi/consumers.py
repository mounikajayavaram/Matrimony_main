# consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("chat", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("chat", self.channel_name)

    async def receive(self, text_data):
        message = json.loads(text_data)['message']

        # Handle the message here (e.g. store it in a database, etc.)

        # Send the message to all connected WebSocket clients
        await self.channel_layer.group_send(
            "chat",
            {
                "type": "chat.message",
                "message": message,
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send the message to the WebSocket client
        await self.send(text_data=json.dumps({
            'message': message
        }))
