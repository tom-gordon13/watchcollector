from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from main_app.forms import ServicingForm

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
  servicing_form = ServicingForm()
  return render(request, 'watches/detail.html', {
    'watch': watch,
    'servicing_form': servicing_form
  })

def add_servicing(request, watch_id):
  form = ServicingForm(request.POST)
  if form.is_valid():
    new_servicing = form.save(commit=False)
    new_servicing.watch_id = watch_id
    new_servicing.save()
  return redirect('detail', watch_id=watch_id)


#Class-based View
class WatchCreate(CreateView):
  model = Watch
  fields = '__all__'

class WatchUpdate(UpdateView):
  model = Watch
  fields = '__all__'

class WatchDelete(DeleteView):
  model = Watch
  success_url = '/watches/'