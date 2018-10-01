import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    city = models.CharField(max_length=255, blank=False, null=False)
    line1 = models.CharField(max_length=255, blank=False, null=False)
    line2 = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=False, null=False)

    def get_absolute_url(self):
        return reverse("basic_app:order_list", kwargs={'pk': self.pk})

    def __str__(self):
        return " City :" + self.city+" , " + "Line: "+self.line1



class Order(models.Model):
    quantity = models.IntegerField(default=1)
    date_placed = models.DateTimeField(db_index=True, default=datetime.datetime.now)
    delivery_date = models.DateTimeField(db_index=True)
    orderedBy = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    total_incl_delivery = models.DecimalField(decimal_places=2, max_digits=12, default=0.0)
    billing_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("basic_app:order_detail", kwargs={'pk': self.pk})
