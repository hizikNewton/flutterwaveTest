import os
import string,random
from django.utils.text import slugify

def random_string(size=10,chars = string.ascii_lowercase+string.digits):
    return  ''.join(random.choice(chars) for _ in range(size))

def unique_slug(instance,new_slug = None):
    '''if new_slug is not None:
        slug = new_slug
    else:'''
    slug = slugify(instance.title)

    klass=instance.__class__
    qs_exist = klass.objects.filter(slug=slug).exists()
    if qs_exist:
        new_slug = '{slug}-{rand_str}'.format(
            slug,
            random_string(size=4)
        )
        return unique_slug(instance,new_slug=new_slug)
    return slug