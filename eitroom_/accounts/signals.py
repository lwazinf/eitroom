from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from profiles.models import manager, tenant

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_tenant==True:
            tenant.objects.create(user=instance)
        elif instance.is_tenant==False:
            manager.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if instance.is_tenant==True:
        instance.tenant.save()
    elif instance.is_tenant==False:
        instance.manager.save()
