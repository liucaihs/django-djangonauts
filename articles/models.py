from django.db import models

class Article(models.Model):
    title   = models.CharField(max_length=100)
    slug    = models.SlugField()
    body    = models.TextField()
    date    = models.DateTimeField(auto_now_add=True)
    thumb   = models.ImageField(default='default.png', blank=True)
    # author

    def __str__(self):
        return self.title

    def snippet(self):
        new_body = self.body[:50]
        if len(new_body) < 50:
            return new_body
        else:
            return new_body + '...'