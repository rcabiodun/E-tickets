from django.db import models
from django.contrib.auth.models import User
from .paystack import PayStack
import secrets
from Account.models import Profile
from datetime import datetime


class Transaction(models.Model):
    user = models.ForeignKey(User, related_name="transaction", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    viewed=models.BooleanField(default=False)
    count=models.IntegerField(null=True,default=0)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.amount)

    def amount_value(self) -> int:
        self.amount+=20
        return self.amount * 100

    def ticket_amount(self) -> int:
        self.amount-=20
        return self.amount



    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            obj_similar = Transaction.objects.filter(ref=ref)
            if not obj_similar:
                self.ref = ref

        super().save(*args, **kwargs)

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            self.amount += 20
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

class Advert(models.Model):
    fullname= models.CharField(max_length=100)
    email= models.EmailField()
    task= models.TextField(max_length=300)
    phone= models.CharField(max_length=11)
    slide=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.fullname
