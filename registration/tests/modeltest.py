# from django.test import TestCase
# from django.urls import reverse
# from user.models import RegistrationPage
# # Create your tests here.
# class RegistrationPageModelTest(TestCase):
#     def setuptestdata(cls):
#         cls.RegistrationPage.objects.create(
#             name='admin',
#             email='admin@gmail.com',
#             mobile_no='12345667',
#             address='delhi',
#             password='admin1234'
#         )
        
#     # def testmodelcontent(self):
#     #     self.assertEqual(self.RegistrationPage.name,'admin')
#     #     self.assertEqual(self.RegistrationPage.email,'admin@gmail.com')
#     #     self.assertEqual(self.RegistrationPage.mobile_no,'12345667')
#     #     self.assertEqual(self.RegistrationPage.address,'delhi')
#     #     self.assertEqual(self.RegistrationPage.password,'admin1234')
        
#     def testurlatcorrectlocation1(self):
#         response=self.client.get("/login/")
#         self.assertEqual(response.status_code,200)
#     def testurlatcorrectlocation2(self):
#         response=self.client.get("/logout/")
#         self.assertEqual(response.status_code,200)
        
        
#     def testurlavailablebyname1(self):
#         response=self.client.get(reverse("login"))
#         self.assertEqual(response.status_code,200)
#     def testurlavailablebyname2(self):
#         response=self.client.get(reverse("logout"))
#         self.assertEqual(response.status_code,200)
        
        
        
#     def testtemplatename1correct(self):
#         response=self.client.get(reverse("registration"))
#         self.assertTemplateUsed(response,"registration.html")
#     def testtemplatename2correct(self):
#         response=self.client.get(reverse("login"))
#         self.assertTemplateUsed(response,"login.html")
#     def testtemplatename3correct(self):
#         response=self.client.get(reverse("logout")) 
#         self.assertTemplateUsed(response,"logout.html")
        
        
#     def testtemplatecontain1(self):
#         response=self.client.get(reverse("registration"))
#         self.assertContains(response,"Register here")
#     def testtemplatecontain2(self):
#         response=self.client.get(reverse("login"))
#         self.assertContains(response,("Login page"))
#     def testtemplatecontain3(self):
#         response=self.client.get(reverse("logout"))
#         self.assertContains(response,("<h1>You are succesfully loggedout..!!!</h1>"))
        
     
#     def testhomepage1(self):
#         response=self.client.get(reverse("login"))
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,"login.html")
#         self.assertContains(response,"Login page")
        
        
#     def testname(self):
#         registrationpage=RegistrationPage.objects.get(id=1)
#         fieldlabel=registrationpage._meta.get_field('name').verbose_name
#         self.assertEqual(fieldlabel,'name')