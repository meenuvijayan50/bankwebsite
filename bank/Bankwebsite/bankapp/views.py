from django.contrib import messages, auth
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


from .forms import PersonCreationForm
from .models import Person, City


# Create your views here.
def demo(request):
    return render(request,"base.html")
def log(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            # return redirect('login')
    return render(request, "login.html")


def register(request):
    return render(request,"register.html")

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, " submitted successfully.")
            form = PersonCreationForm()

    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district_id=district_id).all()
    return render(request, 'forms.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

