from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class TestInstance(models.Model):
    """
    Model representing a specific test instance
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this test instance",
    )
    user = models.ForeignKey(
        "UserSimple", on_delete=models.SET_NULL, null=True)

    date = models.DateTimeField(null=True, auto_now_add=True)
    acet = models.DecimalField(null=True, max_digits=6, decimal_places=3)
    keto = models.DecimalField(null=True, max_digits=6, decimal_places=3)
    par = models.DecimalField(null=True, max_digits=6, decimal_places=3)
    rpm = models.IntegerField(null=True)
    type = models.CharField(max_length=200, blank=True)
    comment = models.TextField(
        max_length=1000, help_text="short comment about test", blank=True)

    class Meta:
        ordering = ["-date"]

    def display_test(self):
        return 'Test of {} {} at {:02d}.{:02d}.{} {:02d}:{:02d}:{:02d}'.format(self.user.first_name, self.user.last_name, self.date.day, self.date.month, self.date.year, self.date.hour, self.date.minute, self.date.second)

    def __str__(self) -> str:
        return self.display_test()


class UserSimple(models.Model):
    """
    Model representing an user. Simple implementation for testing.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
