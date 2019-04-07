from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='image_create', on_delete=models.CASCADE)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='image_liked', blank=True)

    title   = models.CharField(max_length=120)
    slug    = models.SlugField(max_length=120, blank=True, null=True)

    url     = models.URLField(blank=True, null=True)
    image   = models.ImageField(default='default.png', blank = True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Image, self).save(*args, **kwargs)
