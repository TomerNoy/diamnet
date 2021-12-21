import os
import random
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JewelryProject.settings')
django.setup()

from main.models import *

fake = Faker()

# StoneShape.objects.create(shape='Round')
# StoneShape.objects.create(shape='Princess')
# StoneShape.objects.create(shape='Cushion')
# StoneShape.objects.create(shape='Oval')
# StoneShape.objects.create(shape='Emerald')
# StoneShape.objects.create(shape='Pear')
# StoneShape.objects.create(shape='Asscher')
# StoneShape.objects.create(shape='Radiant')
# StoneShape.objects.create(shape='Marquise')
# StoneShape.objects.create(shape='Other')
#
# StoneType.objects.create(type='Sapphire')
# StoneType.objects.create(type='Ruby')
# StoneType.objects.create(type='Emerald')
# StoneType.objects.create(type='Diamond')
#
# Gender.objects.create(type='male')
# Gender.objects.create(type='female')
# Gender.objects.create(type='uni')
#
# MetalColor.objects.create(color='White Gold')
# MetalColor.objects.create(color='Yellow Gold')
# MetalColor.objects.create(color='Rose Gold')
# MetalColor.objects.create(color='Silver')
#
# MetalType.objects.create(type='14k')
# MetalType.objects.create(type='18k')
#
# JewelryShape.objects.create(shape='Ring')
# JewelryShape.objects.create(shape='Necklace')
# JewelryShape.objects.create(shape='Earrings')
# JewelryShape.objects.create(shape='Bracelet')

# temp random images for testing
imgs = [
    'https://www.jeulia.com/media/catalog/product/cache/f8d407e5a8b3027ad7f16791d835e96a/6/0/60419dff5563ejpg.jpg',
    'https://static.smallable.com/1205274-622x622q80/denise-bracelet.jpg',
    'https://cdn.shopify.com/s/files/1/0551/4798/6992/products/christmas-gift-personalized-birthstone-pendent-heart-name-necklace-gold-sparkling-necklace-melodynecklace-29142824058928_1800x1800.jpg?v=1637815342',
    'https://www.jeulia.com/media/catalog/product/cache/f8d407e5a8b3027ad7f16791d835e96a/J/E/JENF000215a61c481bcd19jpg.jpg',
    'https://www.jeulia.com/media/catalog/product/cache/f8d407e5a8b3027ad7f16791d835e96a/5/e/5e8ef36922fdajpg_1.jpg',
    'https://cdn.shopify.com/s/files/1/2226/7715/products/71t209_UsjL._UY575_590x.jpg?v=1548956136',
    'https://cdn.shopify.com/s/files/1/2226/7715/products/71RWP6isVGL._UY1000_590x.jpg?v=1571845776',
    'https://cdn.shopify.com/s/files/1/0550/0272/6575/products/1_4ce5f911-3c2b-4aec-b0a4-96c68d9b58de_700x.jpg?v=1623251256',
    'https://www.jeulia.com/media/catalog/product/cache/f8d407e5a8b3027ad7f16791d835e96a/6/0/607d2e12049b8jpg_1.jpg',
    'https://www.jeulia.com/media/catalog/product/cache/f8d407e5a8b3027ad7f16791d835e96a/5/e/5e16d1829e36fjpg_1.jpg',

    'https://img.mytheresa.com/1088/1088/66/jpeg/catalog/product/43/P00588022.jpg',
    'https://bigamartusax.s3-accelerate.amazonaws.com/2020/07/51WJcfpOjGL._AC_UL1001_.jpg',
    'https://www.jeulia.com/media/catalog/product/cache/f8d407e5a8b3027ad7f16791d835e96a/J/E/JEAR001225c21a49237d87jpg.jpg',
    'https://cdn.shopify.com/s/files/1/0551/4798/6992/products/christmas-gift-personalized-birthstone-pendent-heart-name-necklace-rose-gold-sparkling-necklace-melodynecklace-29142824452144_1800x1800.jpg?v=1637812462',
    'https://watch4u.co.il/wp-content/uploads/2020/01/SZR13.jpg',
    'https://www.jeulia.com/media/catalog/product/cache/f8d407e5a8b3027ad7f16791d835e96a/6/0/608640664a32ajpg_1.jpg',
    'https://cdn.shopify.com/s/files/1/0551/4798/6992/products/christmas-gift-diamond-butterfly-effect-necklace-gold-necklace-melodynecklace-29142758686768_1800x1800.jpg?v=1637853848',
    'https://cfs3.monicavinader.com/images/pdp-small-medium/13279171-set-629.jpg',
    'https://img.fruugo.com/product/2/77/99228772_max.jpg',
    'https://www.jeulia.com/media/catalog/product/cache/f8d407e5a8b3027ad7f16791d835e96a/5/e/5eb276fb08895jpg_1.jpg',

    'https://cdn.shopify.com/s/files/1/2226/7715/products/MNBPSN_1_590x.jpg?v=1598604040',
    'https://cdn2.jomashop.com/media/catalog/product/cache/fde19e4197824625333be074956e7640/h/a/haus-of-brilliance-14k-yellow-gold-plated-925-sterling-silver-15-cttw-solitaire-milgrain-18-pendant-necklace-kl-color-i2i3-clarity-807686ydm.jpg?width=546&height=546',
    'https://img.fruugo.com/product/1/40/166554401_max.jpg',
    'https://cfs3.monicavinader.com/images/pdp-small-medium/13458223-set-649.jpg',
    'https://cdn.shopify.com/s/files/1/2226/7715/products/71-JxdDc7LL._UL1000_590x.jpg?v=1583157397',
    'https://cdn2.jomashop.com/media/catalog/product/cache/fde19e4197824625333be074956e7640/a/m/amour-1-6-ct-diamond-tw-necklace-with-chain-silver-gh-i2_i3-length-_inches_-17-jms005195.jpg?width=546&height=546',
    'https://cdn2.jomashop.com/media/catalog/product/cache/76ca28a553ae7feaf63d5d8d3b95ff3e/a/m/amour-9.66-ct-tgw-oval-lemon-quartz-and-1-2-ct-tw-diamond-necklace-in-14k-yellow-gold-jms005481.jpg?width=546&height=546',
    'https://www.jeulia.com/media/catalog/product/cache/f8d407e5a8b3027ad7f16791d835e96a/5/d/5dd7b307b8beejpg_1.jpg',
    'https://cdn2.jomashop.com/media/catalog/product/cache/fde19e4197824625333be074956e7640/h/a/haus-of-brilliance-14k-white-gold-1-13-ct-tdw-treated-blue-diamond-engagement-ring-blue-si2i1-015595r800.jpg?width=546&height=546',
    'https://cdn.shopify.com/s/files/1/0029/8270/7315/products/fr8216_01_360x.jpg?v=1613315416',
]
for i in range(30):
    Jewelry.objects.create(
        metalType=random.choice(MetalType.objects.all()),
        stoneType=random.choice(StoneType.objects.all()),
        jewelryShape=random.choice(JewelryShape.objects.all()),
        gender=random.choice(Gender.objects.all()),
        stoneShape=random.choice(StoneShape.objects.all()),
        metalColor=random.choice(MetalColor.objects.all()),
        price=round(random.uniform(600, 10000), 2),
        discount=round(random.uniform(-100, 0), 2),
        image=imgs[i]
    )
