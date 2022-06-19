from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=250, blank=True)
    avatar = CloudinaryField('images')
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.SET_NULL, null=True, blank= True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} profile'

class NeighborHood(models.Model):
    hood_name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='hood')
    description = models.TextField()
    health_contact = models.IntegerField(null=True, blank=True)
    police_contact = models.IntegerField(null=True, blank=True)


    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

    def update_neighborhood(self, name):
        self.name = name
        self.save()

    def __str__(self):
        return f'{self.name} neighborhood'