#from datetime import date
#from sre_constants import CATEGORY
#from telnetlib import STATUS
#from unicodedata import category, name
from django.db import models
#from numpy import product

# Create your models here.

class Table(models.Model): 
    FLOOR = (
        ('Ground', 'Ground'),
        ('First', 'First'),
        ('Second', 'Second'),
        ('Fourth', 'Fourth'),
        ('RoofTop', 'RoofTop'),
    )
    table_no = models.IntegerField()
    zone = models.CharField(max_length=50, null=True)
    floor = models.CharField(max_length=50, null=True, choices=FLOOR)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.table_no )

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
            ('Food', 'Food'),
            ('Beverage', 'Beverage'),
            ('Hookah', 'Hookah'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
                ('Pending', 'Pending'),
                ('Served', 'Served'),
            )
    table = models.ForeignKey(Table, null=True, on_delete= models.SET_NULL)
    product= models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
