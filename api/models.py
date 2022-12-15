from django.db import models



class Items(models.Model):
    uri=models.CharField(null=False, max_length=255)
    price=models.CharField(null=False,max_length=255)
    sold=models.BooleanField(default=False)
    itemId=models.IntegerField(default=0)
    category=models.CharField(null=False,max_length=255)
    chain=models.IntegerField(null=False, default=1)
    tokenId=models.IntegerField(null=False, default=1)
    owner=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    auction=models.BooleanField(default=False)
    license=models.BooleanField(default=False)
    contract_address=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    def __str__(self):
        return self.uri

class Userr(models.Model):
    name=models.CharField(null=False,max_length=255)
    address=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    email=models.CharField(null=False,max_length=255,default="examp@ex.com")
    date_joind=models.DateField(auto_now_add=True)
    usename=models.CharField(null=False,max_length=255)
    profile=models.CharField(null=False,max_length=255,default="https://i.imgur.com/KykRUCV.jpeg")
    cover=models.CharField(null=False,max_length=255,default="https://i.imgur.com/jxyuizJ.jpeg")
    def __str__(self):
        return self.name

class Bids(models.Model):
    name=models.CharField(null=False,max_length=255)
    address=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    itemId=models.IntegerField(null=False, default=0)
    chainId=models.IntegerField(null=False, default=0)
    amount=models.CharField(null=False,max_length=255,default="examp@ex.com")
    date_joind=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

