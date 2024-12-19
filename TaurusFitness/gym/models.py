from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Membership(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    start_date = models.DateField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.package.name}"
