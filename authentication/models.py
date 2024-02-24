from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django_countries import countries

class AppUser(AbstractUser):
    is_prime_member = models.BooleanField(default=False, verbose_name="Prime member")
    is_premium_member = models.BooleanField(default=False, verbose_name="Premium member")
    started_prime_subscription = models.DateField(blank=True, null=True)
    started_premium_subscription = models.DateField(blank=True, null=True)
    dob = models.DateField(null=True)
    country = CountryField(default='IN')
    notifications_enabled = models.BooleanField(default=False)


    @property
    def age(self):
        if self.dob:
            today = date.today()
            age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
            return age
        return None

    def __str__(self):
        return self.username