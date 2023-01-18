from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import random 

# Create your models here.
class Kategoria(models.Model):
    emri = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return f'{self.emri}'

class Autori(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    emri = models.CharField(max_length=25)
    mbiemri = models.CharField(max_length=25)
    email = models.EmailField()

    def emri_plote(self):
        return f'{self.emri} {self.mbiemri}'
   
    def __str__(self) -> str:
        return self.emri_plote()

class Lajmi(models.Model):
    titulli = models.CharField(max_length=100, null=False)
    pershkrimi = models.CharField(max_length=200, null=False)
    autori = models.ForeignKey(Autori, on_delete=models.DO_NOTHING)
    kategoria = models.ManyToManyField(Kategoria)
    permbajtja = models.TextField(max_length=500)
    foto = models.ImageField(upload_to="flash")
    data = models.DateField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        int = random.randint(0, 100)
        self.slug = slugify(f'{self.titulli}-{int}')
        super(Lajmi, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.titulli} {self.data}'

    

