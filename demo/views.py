from django.shortcuts import render
from .models import Demo
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.
def booked(request, pk):
	titles = Demo.objects.get(id=pk)


	if titles.booked.filter(id=request.user.id).exists():
		titles.booked.remove(request.user)
	else:
		titles.booked.add(request.user)
	return redirect('home')


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
	context = {
	'title' : title,
	'is_booked' : is_booked,
	}
	return render(request, 'demo/title.html', context)

