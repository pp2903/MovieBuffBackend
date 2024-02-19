from django.db import models
from authentication.models import AppUser
# Create your models here.




class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.user is None:
            # If no user is logged in, set the user field to None
            self.user = None
        super().save(*args, **kwargs)




class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=50)

class TVShow(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=50)



class MovieScript(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed


class Fav(models.Model):
    TYPE_CHOICES = (
        ('movie', 'Movie'),
        ('tvshow', 'TV Show'),
    )
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    favorite_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    item_id = models.IntegerField(default=0)

    class Meta:
        # Ensures each user can only have one favorite entry for each movie or TV show
        unique_together = ('user', 'favorite_type', 'item_id')

    def __str__(self):
        return f"{self.favorite_type}: {self.item_id} "

