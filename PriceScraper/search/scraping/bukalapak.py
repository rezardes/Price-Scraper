from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

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

#keyword = input("Masukkan kata kunci: ")
#print("")
#source = getSource("https://www.bukalapak.com/products?utf8=%E2%9C%93&source=navbar&from=omnisearch&search_source=omnisearch_organic&search[keywords]="+keyword)

#titleList = getTitle(source)
#print(len(titleList))
#for title in titleList:
	#print(title)
#print("")

#priceList = getPrice(source)
#print(len(priceList))
#for price in priceList:
	#print(price)