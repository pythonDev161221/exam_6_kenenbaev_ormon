from django.db import models

# Create your models here.
STATUSCHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Customer(models.Model):
    customer_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="name")
    customer_email = models.EmailField(max_length=254, null=False, blank=False, verbose_name="email")
    order_text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="order_text")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, null=False, blank=False, verbose_name='статус',
                              choices=STATUSCHOICES, default='active')
