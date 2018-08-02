import os,random
from django.db import models
from internTest.utils import unique_slug
from django.db.models.signals import pre_save

def get_file_name(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_img_path(instance,filename):
    appendname = random.randint(1,6467470595606)
    name,ext = get_file_name(filename)
    new_fn = '{appendname}{ext}'.format(appendname=appendname,ext=ext)
    return 'shoes/{new_fn}'.format(new_fn=new_fn)


# Create your models here.
class Shoe(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True,unique=True)
    img = models.ImageField(upload_to=upload_img_path,verbose_name='Upload Image',null=True)
    desc = models.TextField(verbose_name='description')
    price = models.DecimalField(max_digits=19, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/shoes/{slug}/'.format(slug=self.slug)





def shoe_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug(instance)

pre_save.connect(shoe_presave_receiver,sender=Shoe)
