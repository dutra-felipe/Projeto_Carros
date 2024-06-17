from django import forms
from cars.models import Cars, Brand

''' class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) 
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Cars(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car
'''

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 15000:
            self.add_error('value', 'Valor minimo do carro deve ser de R$15.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1960:
            self.add_error('factory_year', 'O ano de fabricação tem que ser superior a 1960')
        return factory_year
    
    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        factory_year = self.cleaned_data.get('factory_year')
        if model_year < factory_year:
            self.add_error('model_year', 'O ano do modelo tem que ser superior ao ano de fabricação')
        return model_year
    
#adicionando forms das BRANDS

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

