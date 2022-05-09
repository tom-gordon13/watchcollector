from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Watch

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def watch_index(request):
    watches = Watch.objects.all()
    return render(request, 'watches/index.html', {
    'watches': watches
  })

def watch_detail(request, watch_id):
  watch = Watch.objects.get(pk=watch_id)
  return render(request, 'watches/detail.html', {
    'watch': watch
  })


#Class-based View
class WatchCreate(CreateView):
  model = Watch
  fields = '__all__'