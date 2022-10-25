from django.db import models
from django.utils import timezone
from django.forms import model_to_dict
from phonenumber_field.modelfields import PhoneNumberField



class Ngo(models.Model):
    name = models.CharField(max_length=100)
    reg_num = models.TextField(max_length=200, default = False)
    address = models.TextField(max_length=200)
    phone = PhoneNumberField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.name

    @property
    def ngo_list(self):
        return self.Ngo.all().values()



class Blog(models.Model):
    tittle = models.CharField(max_length=250)
    details = models.TextField()
    image = models.ImageField(default = False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.tittle

    @property
    def blog_list(self):
        return self.Blog.all().values()




