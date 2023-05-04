# from django.test import TestCase
# # from django.urls import reverse
# from user.forms import *
# # Create your tests here.

# class RegistrationformTest(TestCase):
#     # def setuptestdata(cls):
#     #     cls.RegistrationPage.objects.create(
#     #         name='admin',
#     #         email='admin@gmail.com',
#     #         mobile_no='12345667',
#     #         address='delhi',
#     #         password='admin1234'
#     #     )
    
#     def testregistrationformvalid(self):
#         form=Registrationform(data={'name':"", 'email':"", 'mobile_no':"", 'address':"", 'password':"" })
#         self.assertTrue(form.is_valid())