from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="artwork_post")
    caption = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.caption

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    body = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)


ARTIST_CHOICES = (
    ('becky', 'Becky Johnson'),
    ('alex', 'Alex Anderson'),
    ('john', 'John Masters'),
    ('alison', 'Alison Taylor'),
    ('jasmine', 'Jasmine Evans'),
    ('david', 'David Walker'),
    ('any', 'Any')
)


SUBJECT_CHOICES = (
    ('consultation', 'Free Consultation'),
    ('new', 'New Inquiry'),
    ('reschedule', 'Reschedule Appointment'),
    ('aftercare', 'Aftercare Inquiry'),
    ('other', 'Other'),
)


class Booking(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    artist = models.CharField(max_length=20, choices=ARTIST_CHOICES, default='any')
    subject = models.CharField(max_length=13, choices=SUBJECT_CHOICES, default='other')
    requested_date = models.DateField()
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)


class Review(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    artist = models.CharField(max_length=20, choices=ARTIST_CHOICES, default='any')
    body = models.TextField(max_length=250)
    sent = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)    

    # def __str__(self):
    #     return f"{self.body <br>}by {self.name}"