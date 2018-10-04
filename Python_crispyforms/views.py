from django.shortcuts import render
from django.views.generic import CreateView
from .models import Person

# Create your views here.
def base(request):
    return render(request,'myApp/base.html')



class PersonCreateView(CreateView):
    model = Person
    template_name='myApp/base.html'
    fields = ('name', 'email', 'job_title', 'bio')