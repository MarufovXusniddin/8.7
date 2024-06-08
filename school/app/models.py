from django.db import models

# Create your models here.


class Klass(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f"{self.number}"


class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    klass = models.ManyToManyField(Klass)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name