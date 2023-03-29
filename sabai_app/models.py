from django.db import models

class Tag(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES =[
        ("active", "Active"),
        ("in_active", "Inactive"),
    ]
    title=models.CharField(max_length=200)
    content=models.TextField
    featured_image=models.ImageField(upload_to="post_image/%Y/%m/%d", blank=False)
    published_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    views_count=models.PositiveBigIntegerField(default=0)