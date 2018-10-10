from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .forms import LogMessageForm
from .models import LogMessage


# Create your views here.
def home(request):
    return render(request,'hello/home.html')


def about(request):
    return render(request, 'hello/about.html')


def contact(request):
    return render(request, 'hello/contact.html')

def hello_there(request, name):
    return render (
        request,
        'hello/hello_there.html',
        {
            'name':name,
            'date':datetime.now()
        }
    )


def log_message(request):
    if request.method == 'POST':
        form = LogMessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect('home')

        else:
            form = LogMessageForm()
            return render(request, 'hello/log_message.html', {'form':form})