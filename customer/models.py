from django.db import models


# Create your models here.
class CustomerModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class AddressModel(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
