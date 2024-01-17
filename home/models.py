from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the pending chnages created by makemigrations

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=50)
    openingtime = models.TextField()
    closingtime = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=15)
    order = models.CharField(max_length=50)
    rating = models.TextField()

    def __str__(self):
        return self.name
    
class Shopping(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=50)
    openingtime = models.TextField()
    closingtime = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=15)
    order = models.CharField(max_length=50)
    rating = models.TextField()

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=50)
    openingtime = models.TextField()
    closingtime = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=15)
    order = models.CharField(max_length=50)
    rating = models.TextField()

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.CharField(max_length=50, unique=True)
    areaList = models.TextField()

    def __str__(self):
        return self.user