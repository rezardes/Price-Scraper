import os
import csv

from django.conf import settings
from django.template import Context, loader
from django.http import HttpResponse, Http404

from search.models import BProduk, LProduk

# Create your views here.
def download(request, path):
	#print(path)
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	file_path = os.path.join(BASE_DIR, path)
	#print(file_path)
	if os.path.exists(file_path):
		print('oh')
		with open(file_path, 'rb') as fl:
			response = HttpResponse(fl.read(), content_type="")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404('file does not exist')

def index(request):
	template = loader.get_template("index.html")
	context = {
		'Nil': '-'
	}
	return HttpResponse(template.render(context,request))

def unduh(request):

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	file_path = os.path.join(BASE_DIR, 'names.csv')
	print(file_path)
	'''
	with open(file_path, 'w') as csvfile:
		fieldnames = ['first_name', 'last_name']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
		writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
		writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
	'''
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="bukalapak.csv"'

	writer = csv.writer(response)
	writer.writerow(['Produk', 'Harga', 'Link Gambar'])
	daftar = []
	bukalapak_list = BProduk.objects.order_by("price")
	for product in bukalapak_list:
		daftar.append(product.name)
		daftar.append(product.price)
		daftar.append(product.imageURL)
		writer.writerow(daftar)
		daftar = []

	return response