import os

from django.conf import settings
from django.template import Context, loader
from django.http import HttpResponse, Http404

# Create your views here.
def download(request, path):
	#print(path)
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	file_path = os.path.join(BASE_DIR, path)
	print(file_path)
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