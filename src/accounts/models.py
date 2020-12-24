from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in
import time


class User(AbstractUser):
    """
    Modified User Model to add employee_id field
    """

    employee_id = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    login_count = models.PositiveIntegerField(default=0)

    def login_user(sender, request, user, **kwargs):
        """
        Function connected to a signal that triggers whenever
        user loggs in and increments login_count number.
        """
        user.login_count += 1
        user.save()

    def save(self, *args, **kwargs):
        """
        Overides the save method to make sure if employee_id
        is left blank it will get a unique value
        """
        if self.employee_id == "":
            self.employee_id = str(
                int(time.time())
            )  # int() to get rid of number behind the dot. (5684231.65481 to 5684231)
            # str() to turn it into a string. (5684231 to "5684231")
        super().save(*args, **kwargs)

    user_logged_in.connect(login_user)  # Connects singal to a function
