from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver



# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Images/slider.jpg')
    entry1= models.CharField(max_length=255)
    entry2= models.CharField(max_length=255)
    link= models.CharField(max_length=255,default="#")


    def __str__(self):
        return self.title[:40]
    





class mainCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title[:40]


class Category(models.Model):
    title = models.CharField(max_length=255)
    mainCategory = models.ForeignKey(mainCategory,null=True,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title[:40]

class subCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:40] 
    


class Product(models.Model):
    title = models.CharField(max_length=255,null=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    price = models.PositiveBigIntegerField(default=0,null=True)
    discount = models.PositiveIntegerField(default=0,null=True)
    featured_image = models.CharField(max_length=255,null=True)
    brand = models.CharField(max_length=255,null=True)
    total = models.PositiveIntegerField(default=0,null=True)
    available = models.PositiveIntegerField(default=0,null=True)
    description = RichTextField(null=True,blank=True)
    product_information = RichTextField(null=True,blank=True)
    tags = models.CharField(max_length=255,null=True,blank=True)
    slug = models.CharField(max_length=555,null=True,blank=True)

    def __str__(self):
        return self.title[:40] 


@receiver(pre_save,sender=Product)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.title)
        unique_slug=base_slug

        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug=f"{base_slug}-{instance.id}"
        instance.slug = unique_slug    

class Additional_information(models.Model):
        product = models.ForeignKey(Product,on_delete=models.CASCADE)
        title = models.CharField(max_length=255,null=True,blank=True)
        spec = models.CharField(max_length=255,null=True,blank=True)

class Additional_image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.CharField(max_length=555,null=True,blank=True)     


