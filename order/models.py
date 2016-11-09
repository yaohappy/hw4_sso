from django.db import models


class Order(models.Model):
    order_id = models.CharField(max_length=20)
    customer = models.CharField(max_length=20)
    item = models.CharField(max_length=20)

    def __str__(self):
        return self.order_id
