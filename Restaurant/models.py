from django.db import models
# Ensure price and inventory not below a certain number
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Booking(models.Model):
    ID = models.IntegerField(primary_key= True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()
    
    def __str__(self):
        return self.Name
    
class Menu(models.Model):
    ID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits = 10,decimal_places=2,
    validators = [
        MaxValueValidator(20.00),
        MinValueValidator(2.00)
        ]                          
    )
    Inventory = models.IntegerField(
        null=False,
        validators =[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    
    def __str__(self):
        return f'{self.Title}:{str(self.Price)}'
    
    