from django.template import Context, loader
from django.http import HttpResponse

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#from .scraping import bukalapak

def getSource(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(), "html.parser")
	except AttributeError as e:
		return None
	return bsObj

class Product(object):
	"""docstring for Product"""
	def __init__(self, name, price):
		self.name = name
		self.price = price

def getProduct(soup):
	hasil = []
	counter = 0
	price_src = soup.find_all("div","product-price")
	for name in soup.find_all("div","product-description"):
		hasil.append(Product(name.h3.a.get_text(),price_src[counter]["data-reduced-price"]))
		counter = counter+1
	return hasil
'''
def getTitle(soup):
	hasil = []
	for title in soup.find_all("div","product-description"):
		hasil.append(title.h3.a.get_text())
	return hasil

def getPrice(soup):
	hasil = []
	for harga in soup.find_all("div","product-price"):
		hasil.append(harga["data-reduced-price"])
	return hasil
'''

# Create your views here.
def index(request):
	template = loader.get_template("search\searching.html")
	soup = getSource("https://www.bukalapak.com/products?utf8=%E2%9C%93&source=navbar&from=omnisearch&search_source=omnisearch_organic&search[keywords]=kangguru")
	
	product_list = getProduct(soup)

	context = {
		'product_list': product_list,
	}
	return HttpResponse(template.render(context,request))