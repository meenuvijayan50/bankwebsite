from django.db import models
from django.db.models import Model


# Create your models here.
# Gender_choices=(('female','FEMALE'),
#                  ('male','MALE'),
#                 ('trangender','TRANSGENDER'),)
# Material_choices=(('debit card','DEBIT CARD'),
#                   ('credit card','CREDIT CARD'),
#                   ('cheque','CHEQUE'))
class District(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Branches(models.Model):
    branches = models.ForeignKey(District, on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class User(models.Model):
    name=models.CharField(max_length=200)
    DOB=models.DateField()
    age=models.IntegerField()
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()

    District = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branches = models.ForeignKey(Branches, on_delete=models.SET_NULL, blank=True, null=True)
    Account = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)

    Material_choices = (('debit card', 'DEBIT CARD'),('credit card','CREDIT CARD'),('cheque','CHEQUE'))
    materials_provided=models.CharField(max_length=20,choices= Material_choices)

    def __str__(self):
        return self.name





