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
        verbose_name = 'categories'
        verbose_name_plural = 'Categories'

# Create your models here.
class Posts(models.Model):
    # title =   models.CharField(max_length=50,validators=[validators.validate_email,validators])
    # def check_minlenth(val):
        # if len(val) < 10:
        #     raise validators.ValidationError('Ti must be greter then 10')

    # title =   models.CharField(max_length=50,validators=[check_minlenth])
    title =   models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1,null=True)
    content = models.TextField()
    thumbnail = models.FileField(upload_to="posts/",null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'posts' #table name in database 
        verbose_name = 'Posts' # Show in admin for sigular
        verbose_name_plural = 'Posts' # shwo in admin for plurals

#create a form these form will be shown on model template
class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields= ['title','content','thumbnail','user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter email'}),
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder':'write here'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'user'  : forms.Select(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'Title(Enter Youer Name)'
        }
        help_texts = {
            'title': ('Some useful help text.'),
        }
        error_messages = {
            'title':{
                'max_length': 'Abe 50 se jata charcter enter mat kar'

            }
        }
        
    
    # def clean(self):
    #     fields = self.cleaned_data
    #     keys    = list(fields.keys())
    #     if(len(fields['title']) < 10 ):
    #         raise validators.ValidationError(f"{keys[0]} must be grater then 10 ")

        

