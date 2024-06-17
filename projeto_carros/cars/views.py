from cars.models import Cars, Brand
from cars.forms import CarModelForm, BrandForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, ListView, CreateView, DetailView, UpdateView

class CarsListView(ListView):
    model = Cars
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Cars
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class CarDetailView(DetailView):
    model = Cars
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model= Cars
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Cars
    template_name = 'car_delete.html'
    success_url = '/cars/'

#criando view de Brands
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewBrandView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'new_brand.html'
    success_url = reverse_lazy('cars_list')

    def form_valid(self, form):
        return super().form_valid(form)