from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#user here is the default and the class under is adding to it
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
#to add more attributes - extending the class
    #additional classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

#to print
    def __str__(self):
        return self.user.username

#installed pillow to work with images

#ordering
class UserOrders(models.Model):
    user_order = models.IntegerField()
    orderedBy = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, null=True)
#    orderedBy = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE,null=True,blank=True,default="Khoury",related_name="orders")
