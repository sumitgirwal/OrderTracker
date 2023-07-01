from django.db import models

# Create your models here.
class Dish(models.Model):
    title = models.CharField(max_length=100)
    description  = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=1)

    def __str__(self):
        return self.title


STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

class Order(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.status}"
