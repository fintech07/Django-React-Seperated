from django.test import TestCase
from .models import Scrap

class ScrapModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Scrap.objects.create(title='first scrap')
        Scrap.objects.create(description='hehe')

    def test_title_content(self):
        scrap = Scrap.objects.get(id=1)
        expected_object_name=f'{scrap.title}'
        self.assertEquals(expected_object_name, 'first scrap')

    def test_description_content(self):
        scrap = Scrap.objects.get(id=2)
        expected_object_description = f'{scrap.description}'
        self.assertEquals(expected_object_description, 'hehe')
