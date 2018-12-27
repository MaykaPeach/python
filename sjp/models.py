from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    balance = models.FloatField(null=False, default=0)
    name = models.CharField(max_length=30, null=False)
    #reputation = models.FloatField(null=False, default=0)

    def get_absolute_url(self):
        return reverse('sjp:user-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.username


class Purchase(models.Model):
    allCash = models.FloatField(null=False)
    nowCash = models.FloatField(null=False, default=0)
    status = models.BooleanField(null=False, default=True)
    id_author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    #allCountProducts = models.IntegerField()
    #pricePerProduct = models.FloatField()

    def get_absolute_url(self):
        return reverse('sjp:purchase-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class JointPurchase(models.Model):
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)
    id_purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE)
    expense = models.FloatField(null=False) #аванс, внесенный пользователем

    def get_absolute_url(self):
        return reverse('sjp:joint-purchase-detail', kwargs={'pk': self.pk})