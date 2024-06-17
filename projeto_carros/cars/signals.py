from django.db.models.signals import post_delete, post_save, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Cars, CarInventory
#form openai_api.client import get_car_ai_bio

def car_inventory_update():
    car_count = Cars.objects.all().count()
    car_value = Cars.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count = car_count,
        cars_value = car_value
    )

@receiver(pre_save, sender=Cars)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        #ai_bio = get_car_ai_bio(instance.model, instance.brand, instance.model_year)
        instance.bio = 'Bio gerada automaticamente!' #substituir por ai_bio

@receiver(post_save, sender=Cars)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Cars)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
