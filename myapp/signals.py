from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order 

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Order)
def update_status(sender, instance, created, **kwargs):
    # send to channels
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'public_room',
            {
                "type": "send_notification",
                "message": instance.message
            }
        )
    print("$##############################")
    print(instance)
    print("$##############################")