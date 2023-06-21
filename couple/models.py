from django.db import models

class Couple(models.Model):
    man = models.ForeignKey("account.User",on_delete = models.CASCADE, related_name = "man")
    woman = models.ForeignKey("account.User",on_delete = models.CASCADE, related_name = "woman")
