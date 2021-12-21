from django.db import models
from account.models import Profile
from main.models import Jewelry


class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    is_ordered = models.BooleanField(default=False)
    jewelries = models.ManyToManyField(Jewelry)
    date = models.DateTimeField(auto_now_add=True)

    def get_cart_total(self):
        print(sum(item.price for item in self.jewelries.all()))
        return sum([item.price for item in self.jewelries.all()])

    def __str__(self):
        return f'count: {len(self.jewelries.all())}'


class Transaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
