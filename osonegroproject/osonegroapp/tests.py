from django.test import TestCase
from .models import Product, RecordType, Review


class ProductTypeTest(TestCase):
   def test_string(self):
       type=RecordType(recordname="Tablet")
       self.assertEqual(str(type), type.recordname)

   def test_table(self):
       self.assertEqual(str(RecordType._meta.db_table), 'recordtype')
