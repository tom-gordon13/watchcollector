from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from main_app.forms import ServicingForm

from .models import Watch, Component

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
  id_list = watch.components.all().values_list('id')
  missing_comp = Component.objects.exclude(id__in=id_list)
  servicing_form = ServicingForm()
  return render(request, 'watches/detail.html', {
    'watch': watch,
    'servicing_form': servicing_form, 
    'components': missing_comp,
  })

def add_servicing(request, watch_id):
  form = ServicingForm(request.POST)
  if form.is_valid():
    new_servicing = form.save(commit=False)
    new_servicing.watch_id = watch_id
    new_servicing.save()
  return redirect('detail', watch_id=watch_id)

def assoc_comp(request, watch_id, component_id):
  Watch.objects.get(id=watch_id).components.add(component_id)
  return redirect('detail', watch_id=watch_id)

#Class-based View
class WatchCreate(CreateView):
  model = Watch
  fields = ['make', 'model', 'year', 'price']

class WatchUpdate(UpdateView):
  model = Watch
  fields = '__all__'

class WatchDelete(DeleteView):
  model = Watch
  success_url = '/watches/'

#Class-based Views for Component
class ComponentList(ListView):
  model = Component

class ComponentDetail(DetailView):
  model = Component

class ComponentCreate(CreateView):
  model = Component
  fields = '__all__'
  success_url = '/components/'

class ComponentUpdate(UpdateView):
  model = Component
  fields = '__all__'

class ComponentDelete(DeleteView):
  model = Component
  success_url = '/components/'