from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Core(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Item(Core):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Bid(Core):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.item.name + " - " + self.bidder.username + " - " + str(self.bid)
    
class Auction(Core):
    statuses = (
        ('I', 'Inactive'),
        ('O', 'Open'),
        ('C', 'Closed'),
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=statuses, default='I')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    def __str__(self):
        return self.item.name + " - " + str(self.start_date) + " - " + str(self.end_date)
