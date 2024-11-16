from django.db import models

# Create your models here.
class Record(models.Model):
    Created_at  = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=260)
    emali = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    adress = models.CharField(max_length=10000)
    city = models.CharField(max_length=290)
    Region = models.CharField(max_length=390)
    zipcod = models.CharField(max_length=50)

    def __str__(self):
        return(f'{self.first_name} {self.last_name}')
    


