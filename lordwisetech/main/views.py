from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import data


# Create your views here.


class showdata(ListView):
    model = data
    template_name = "main/template/index.html"


def hello(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        mobie = request.POST['mobie']
        skils = request.POST['skils']

        new_data = data(name=name, surname=surname, mobie=mobie, skills=skils)
        new_data.save()
    return render(request, "main/template/add.html")


def delete(request, pk):
    getdelete = data.objects.get(id=pk)
    getdelete.delete()
    return redirect("showdataurl")

def update(request, pk):
    getupdate = data.objects.get(id=pk)

    if request.method == 'POST':
        getupdate.name = request.POST['name']
        getupdate.surname = request.POST['surname']
        getupdate.mobie = request.POST['mobie']
        getupdate.skills = request.POST['skils']
        getupdate.save()
        return redirect("showdataurl")
    context = {'post': getupdate}
    return render(request,"main/template/updatee.html",context)



