from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order 

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Order)
def status_created(sender, instance, created, **kwargs):
    # send to channels
    if instance:
        percentage = 0
        if instance.status == 'pending':
            percentage = 15
        elif instance.status == 'processing':
            percentage = 75
        else:
            percentage = 100

        
        print("Now: $##############################")
        print(instance, instance.status, percentage)
        

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'order_status',
            {
                "type": "update_status",
                "status": instance.status,
                "percentage": percentage
            }
        )
        print("Now, $##############################")
    
    print("NoT Working..............................")