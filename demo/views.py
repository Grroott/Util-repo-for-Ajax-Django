from django.shortcuts import render
from .models import Demo
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
# Create your views here.
def booked(request, pk):
	title = Demo.objects.get(id=pk)

	is_booked = False
	if title.booked.filter(id=request.user.id).exists():
		is_booked = True
	


	if title.booked.filter(id=request.user.id).exists():
		title.booked.remove(request.user)
	else:
		title.booked.add(request.user)
	# return redirect('home')

	cou = title.booked.count()

	if request.is_ajax():
		context = {
		'title' : title,
		'is_booked' : is_booked,
		'cou' : cou
		}
		html = render_to_string('demo/title.html', context, request=request)
		return JsonResponse({'form': html})

def home(request):
	titles = Demo.objects.all()
	context = {
	'titles' : titles
	}

	return render(request, 'demo/home.html', context)
def titles(request, pk):
	title = Demo.objects.get(id=pk)
	is_booked = False
	if title.booked.filter(id=request.user.id).exists():
		is_booked = True
	cou = title.booked.count()
	context = {
	'title' : title,
	'is_booked' : is_booked,
	'cou' : cou
	}
	return render(request, 'demo/title.html', context)

