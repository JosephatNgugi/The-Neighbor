from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # name = models.CharField(max_length=80, blank=True)
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
    location = models.CharField(max_length=200, null=True)
    health_contact = models.IntegerField(null=True, blank=True)
    police_contact = models.IntegerField(null=True, blank=True)


    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

    def update_neighborhood(self, hood_name):
        self.hood_name = hood_name
        self.save()

    def __str__(self):
        return f'{self.hood_name} neighborhood'
    
class Business(models.Model):
    business_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner')

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(business_name__icontains=name).all()

    def __str__(self):
        return f'{self.business_name} Business'

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')


    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def __str__(self):
        return self.title