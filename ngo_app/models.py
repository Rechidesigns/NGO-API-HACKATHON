from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Ngo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    reg_num = models.TextField(max_length=200, blank=True, null=True)
    address = models.TextField(max_length=200)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name



STATUS = (("draft","Draft"), 
              ("published","Published"))


class Blog(models.Model):
    tittle = models.CharField(max_length=250)
    details = models.TextField()
    image = models.ImageField(upload_to='NGOblogpic', null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    published = models.CharField(max_length=50, choices=STATUS, default="published")

    class Meta:
        ordering = ('-published',)

    def _str_(self):
        return self.tittle







