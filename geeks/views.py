from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm


def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = GeeksForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)

def list_view(request):
	context = {}
	context["dataset"] = GeeksModel.objects.all()

	return render(request, "list_view.html", context)

def detail_view(request, id):
	context = {}
	context["data"] = GeeksModel.objects.get(id = id)
	return render(request, "detail_view.html", context)

def update_view(request, id):
	context = {}

	obj = get_object_or_404(GeeksModel, id = id)
	form = GeeksForm(request.POST or None, instance = obj)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/list/"+id)
	
	context["form"] = form

	return render(request, "update_view.html", context)

def delete_view(request, id):
	context = {}

	obj = get_object_or_404(GeeksModel, id = id)

	if request.method == "POST":
		obj.delete()

		return HttpResponseRedirect("/list")

	return render(request, "delete_view.html", context)
