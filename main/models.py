from django.core.exceptions import ValidationError
from django.db import models


class StoneShape(models.Model):
    SHAPE = [
        ('BR', 'Round'),
        ('PC', 'Princess'),
        ('CU', 'Cushion'),
        ('OV', 'Oval'),
        ('EM', 'Emerald'),
        ('PS', 'Pear'),
        ('AC', 'Asscher'),
        ('RA', 'Radiant'),
        ('MQ', 'Marquise'),
        ('O', 'Other'),
    ]
    shape = models.CharField(max_length=20, choices=SHAPE, unique=True)

    def __str__(self):
        return self.shape


class StoneType(models.Model):
    TYPE = [('S', 'Sapphire'), ('R', 'Ruby'), ('E', 'Emerald'), ('D', 'Diamond')]
    type = models.CharField(max_length=10, choices=TYPE, unique=True)

    def __str__(self):
        return self.type


class Gender(models.Model):
    TYPE = [('male', 'male'), ('female', 'female'), ('uni', 'uni')]
    type = models.CharField(max_length=10, choices=TYPE, unique=True)

    def __str__(self):
        return self.type


class MetalColor(models.Model):
    COLOR = [('W', 'White Gold'), ('Y', 'Yellow Gold'), ('R', 'Rose Gold'), ('S', 'Silver')]
    color = models.CharField(max_length=20, choices=COLOR, unique=True)

    def __str__(self):
        return self.color


class MetalType(models.Model):
    TYPE = [('14k', '14k'), ('18k', '18k')]
    type = models.CharField(max_length=20, choices=TYPE, unique=True)

    def __str__(self):
        return self.type


class JewelryShape(models.Model):
    SHAPE = [('R', 'Ring'), ('N', 'Necklace'), ('E', 'Earrings'), ('B', 'Bracelet')]
    shape = models.CharField(max_length=20, choices=SHAPE, unique=True)

    def __str__(self):
        return self.shape


class Jewelry(models.Model):
    metalType = models.ForeignKey(MetalType, on_delete=models.CASCADE)
    stoneType = models.ForeignKey(StoneType, on_delete=models.CASCADE)
    jewelryShape = models.ForeignKey(JewelryShape, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    stoneShape = models.ForeignKey(StoneShape, on_delete=models.CASCADE, null=True)
    metalColor = models.ForeignKey(MetalColor, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    image = models.URLField(max_length=300)
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.stoneType} {self.stoneShape} {self.metalColor} {self.jewelryShape} {self.metalType}'
