from django.test import TestCase
from .models import Kategoria,Lajmi,Autori

# Create your tests here.
class KategoriaClassTest(TestCase):
    def setUp(self):
        Kategoria.objects.create(emri='test')


class AutoriClassTest(TestCase):
    def setUp(self):
        Autori.objects.create(user_name=1, emri='user_test', mbiemri='test_mbiemri', email='test@test.com')

class LajmiClassTest(TestCase):
    def setUp(self):
        Lajmi.objects.create(titulli='',
                             pershkrimi='',
                             autori =1,
                             kategoria =1,
                             permbajtja= 'test',
                             fot = 'images/logo.png',
                             data = 1/23/2023,
                             slug = 'test-1'       )
    
