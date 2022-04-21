from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(default = 'John(default)', max_length=200, null=True)

    last_name = models.CharField(default = 'Doe(default)', max_length=200, null=True)

    emaail = models.CharField(default = 'user@gmail.com', max_length=300, null=True)

    profile_img = models.ImageField(default='media/default.jpg', upload_to='media', null=True, blank = True)

    def __str__(self):
        return f"{self.user.username}'s account"
# Create your models here.
