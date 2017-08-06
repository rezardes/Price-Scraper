import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()

from .models import BProduk, LProduk
BProduk.objects.all().delete()
LProduk.objects.all().delete()
'''
p = Produk,objects.get()
p.entry_set.clear()
'''
'''
def populate(product_list):
	for product in product_list:
		add_product(product.name, product.price, product.url)
	return None
'''
def add_product(name,price,url,keyword):
	if (keyword == "bukalapak"):
		p = BProduk.objects.get_or_create(name=name, price=price, imageURL=url)[0]
		p.save()
	else:
		p = LProduk.objects.get_or_create(name=name, price=price, imageURL=url)[0]
		p.save()
	return p