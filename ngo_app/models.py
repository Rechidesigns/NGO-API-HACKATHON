from django.db import models
from django.utils import timezone
from django.forms import model_to_dict
from phonenumber_field.modelfields import PhoneNumberField

STATUS = (("unpublished","Unpublished"), 
              ("published","Published"))
    

class Ngo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    reg_num = models.TextField(max_length=200, blank=True, null=True)
    address = models.TextField(max_length=200)
    phone = PhoneNumberField()
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

    @property
    def ngo_list(self):
        return self.Ngo.all().values()



class Blog(models.Model):
    tittle = models.CharField(max_length=250)
    details = models.TextField()
    image = models.ImageField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default="published")

    STATUS = (("unpublished","Unpublished"), 
              ("published","Published"))

    def _str_(self):
        return self.tittle

    @property
    def blog_list(self):
        return self.Blog.all().values()




