from django.shortcuts import render

# Create your views here.
def xmasletters_page(request):
	return render(request, 'cover.html')

def home_page(request):
	return render(request, 'home.html')

def makeletter_page(request):
	return render(request, 'makeletter.html')

def worldletters_page(request):
	return render(request, 'worldletters.html')