from django.db import models
from django.contrib.auth.models import AbstractUser
import time


class User(AbstractUser):
    """
    Modified User Model to ad employee_id field
    """

    employee_id = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        """
        Overides the save methot to make sure if employee_id
        is left blank it will get a unique value
        """
        if self.employee_id == "":
            self.employee_id = str(
                int(time.time())
            )  # int() to get rid of number behind the dot. (5684231.65481 to 5684231)
            # str() to turn it into a string. (5684231 to "5684231")
        super().save(*args, **kwargs)
