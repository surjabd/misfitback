# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from Data.models import acce_data


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message = text_data_json['message']
        xdata=text_data_json['data_x']
        ydata = text_data_json['data_y']
        zdata = text_data_json['data_z']
        device = text_data_json['device_id']

        #SAVE DATA
        acce_data.objects.create(device_id=device,data_x=xdata,data_y=ydata,data_z=zdata)

        print(text_data)



        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'device_id': device,
                'data_x': xdata,
                'data_y': ydata,
                'data_z': zdata
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        xdata = event['data_x']
        ydata = event['data_y']
        zdata = event['data_z']
        device = event['device_id']
        print("When are we working")
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'device_id': device,
            'data_x': xdata,
            'data_y': ydata,
            'data_z': zdata
        }))