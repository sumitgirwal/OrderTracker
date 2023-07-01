from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.template.loader import get_template

class StatusConsumer(WebsocketConsumer):
    def connect(self):
        self.GROUP_NAME = 'order_status'
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
         
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP_NAME, self.channel_name
        )

    def update_status(self, event):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        html = get_template("progress.html").render(
            context={
                "percentage": event["percentage"],
                "status": event["status"]
            }
        )
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        self.send(text_data=html)