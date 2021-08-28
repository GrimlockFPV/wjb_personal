from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

CATEGORIES = [
    ('MKT', 'Marketing'),
    ('P3D', '3D Printing'),
    ('FPV', 'FPV Drones'),
    ('WII', 'Portables'),
    ('WEB', 'Web Development'),
    ('COD', 'Other Coding'),
    ("OEE", 'Other Electronics'),
    ('SKI', 'Outdoors'),
    ('SPT', 'Sports'),
    ('KID', 'Kids'),
]


class Category(models.Model):

    name = models.CharField(choices=CATEGORIES, max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):

    STATUS = [('D', 'Draft'), ('P', 'Publish')]

    FEATURED = [('P', 'Primary'), ('S', 'Secondary')]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    preview = models.CharField(max_length=255)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    featured = models.CharField(max_length=1, choices=FEATURED, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='D')
    category = models.CharField(max_length=200, choices=CATEGORIES, default='WEB')
    image = models.ImageField(blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
