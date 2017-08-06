from django.template import Context, loader
from django.http import HttpResponse
from django.db import models

import json

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

from .populate import add_product
from .models import BProduk, LProduk

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
	def __init__(self, name, price, link):
		self.name = name
		self.price = price
		self.link = link

def getProductBukalapak(soup):
	#hasil = []
	counter = 0
	price_src = soup.find_all("div","product-price")
	image_src = soup.find_all("picture","product-picture")
	#print(image_src)
	for name in soup.find_all("div","product-description"):
		add_product(name.h3.a.get_text(),price_src[counter]["data-reduced-price"],
			image_src[counter].find("img")["data-src"],"bukalapak")
		counter = counter+1
	return BProduk.objects.order_by("price")

def getProductLazada(soup):
	#hasil = []
	json_string=soup.head.find("script").get_text()
	parsed_json = json.loads(json_string)
	#print(len(parsed_json["itemListElement"]))
	itemListElement = parsed_json["itemListElement"]
	for item in itemListElement:
		product_name = item["name"]
		product_img = item["image"]
		product_price = item["offers"]["price"]
		add_product(product_name,product_price[:-3],product_img,"lazada")
		#hasil.append( Product(product_name,product_price,product_img) )
	return LProduk.objects.order_by("price")
	'''
	for script in script_list:
		print(script)
	'''
# Create your views here.
def index(request):
	search_text = request.GET.get('q','')
	search_text = search_text.replace(' ','+')
	template = loader.get_template("search/searching.html")
	print(search_text)
	soup = getSource("https://www.bukalapak.com/products?utf8=%E2%9C%93&source=navbar&from=omnisearch&search_source=omnisearch_organic&search[keywords]="+search_text)
	soup2 = getSource("http://www.lazada.co.id/catalog/?q="+search_text)
	lazada_list = getProductLazada(soup2)
	bukalapak_list = getProductBukalapak(soup)
	#product_list = getProduct(soup)

	context = {
		'lazada_list': lazada_list,
		'bukalapak_list': bukalapak_list,
	}
	
	return HttpResponse(template.render(context,request))