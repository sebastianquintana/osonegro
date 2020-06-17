from django.db import models
from django.contrib.auth.models import User

class RecordType(models.Model):
    recordname=models.CharField(max_length=255)
    recorddescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.recordname
    
    class Meta:
        db_table='recordtype'
        verbose_name_plural='recordtypes'

class Product(models.Model):
    productname=models.CharField(max_length=255)
    producttype=models.ForeignKey(RecordType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    productprice=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    productentrydate=models.DateField()
    producturl=models.URLField(null=True, blank=True)
    productdescription=models.TextField()

    def memberdiscount(self):
        discountpercent=.05
        return float(self.productprice) * discountpercent

    def __str__(self):
        return self.productname
    
    class Meta:
        db_table='product'
        verbose_name_plural='products'


class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ManyToManyField(User)
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='review'
        verbose_name_plural='reviews'
