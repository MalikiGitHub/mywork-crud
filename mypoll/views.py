from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from .forms import PollForm

from .models import Poll
# Create your views here.
def home(request):
    if 'category' in request.GET:
        q=request.GET['category']
        poll = Poll.objects.filter(categories__icontains=q)
    else:
        poll = Poll.objects.all()
    return render(request, 'mypoll/index.html', {'poll':poll})


def poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your Post has been updated")
            return redirect('home')
    else:
        form = PollForm()
        
    return render(request, 'mypoll/poll.html', {'form':form})


def editpoll(request, pk):
    poll = Poll.objects.get(id=pk)
    
    if request.method == 'POST':
        form = PollForm(request.POST, instance=poll)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PollForm(instance=poll)  
    return render(request, 'mypoll/poll.html', {'form':form})
        
    