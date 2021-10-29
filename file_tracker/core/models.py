from django.db import models

class user_entry(models.Model):
    file_id = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    port = models.CharField(max_length=4)
    user_id = models.CharField(max_length=200)
    time = models.TimeField(auto_now_add=True)
