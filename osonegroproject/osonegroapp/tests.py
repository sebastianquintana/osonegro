from django.test import TestCase
from .models import Product, RecordType, Review
from django.urls import reverse
from django.contrib.auth.models import User


class ProductTypeTest(TestCase):
   def test_string(self):
       type=RecordType(recordname="Tablet")
       self.assertEqual(str(type), type.recordname)

   def test_table(self):
       self.assertEqual(str(RecordType._meta.db_table), 'recordtype')

class ProductTest(TestCase):
   #set up one time sample data
   def setup(self):
       type = ProductType(typename='laptop')
       product=Product(productname='Lenovo', producttype=type, productprice='500.00')
       return product
   def test_string(self):
       prod = self.setup()
       self.assertEqual(str(prod), prod.productname)
  
   #test the discount property
   def test_discount(self):
       prod=self.setup()
       self.assertEqual(prod.memberdiscount(), 25.00)

   def test_type(self):
       prod=self.setup()
       self.assertEqual(str(prod.producttype), 'laptop')

   def test_table(self):
       self.assertEqual(str(Product._meta.db_table), 'product')


class ReviewTest(TestCase):
   def test_string(self):
       rev=Review(reviewtitle="Best Review")
       self.assertEqual(str(rev), rev.reviewtitle)

   def test_table(self):
       self.assertEqual(str(Review._meta.db_table), 'review')


class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetProductsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('products'))
       self.assertEqual(response.status_code, 200)

def setUp(self):
        self.u=User.objects.create(username='myuser')
        self.type=RecordType.objects.create(recordname='luismiguel')
        self.prod = Product.objects.create(productname='product1', producttype=self.type, user=self.u, productprice=500, productentrydate='2019-04-02', productdescription="a product")
        self.rev1=Review.objects.create(reviewtitle='prodreview', reviewdate='2019-04-03', product=self.prod, reviewrating=4, reviewtext='some review')
        self.rev1.user.add(self.u)
        self.rev2=Review.objects.create(reviewtitle='prodreview', reviewdate='2019-04-03', product=self.prod,  reviewrating=4, reviewtext='some review')
        self.rev2.user.add(self.u)

def test_product_detail_success(self):
        response = self.client.get(reverse('productdetails', args=(self.prod.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)

def test_discount(self):
        discount=self.prod.memberdiscount()
        self.assertEqual(discount, 25.00)

def test_number_of_reviews(self):
        reviews=Review.objects.filter(product=self.prod).count()
        self.assertEqual(reviews, 2)
