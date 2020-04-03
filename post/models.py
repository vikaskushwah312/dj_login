from django.db import models
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def check_minlenth(val):
    if len(val) < 10:
        raise validators.ValidationError('Ti must be greter then 10')

class Category(models.Model):
    title = models.CharField(validators=[check_minlenth],max_length=10)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = models.Manager

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'categories'

# Create your models here.
class Posts(models.Model):
    # title =   models.CharField(max_length=50,validators=[validators.validate_email,validators])
    # def check_minlenth(val):
        # if len(val) < 10:
        #     raise validators.ValidationError('Ti must be greter then 10')

    # title =   models.CharField(max_length=50,validators=[check_minlenth])
    title =   models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'posts'

#create a form these form will be shown on model template
class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields= ['title','content','user']
    
    # def clean(self):
    #     fields = self.cleaned_data
    #     keys    = list(fields.keys())
    #     if(len(fields['title']) < 10 ):
    #         raise validators.ValidationError(f"{keys[0]} must be grater then 10 ")

        

