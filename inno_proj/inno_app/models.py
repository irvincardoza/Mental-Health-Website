from django.db import models
# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# Create your models here.
class Upload(models.Model):
    first_name = models.CharField(max_length=128)

    story_text = models.CharField(max_length=200)
