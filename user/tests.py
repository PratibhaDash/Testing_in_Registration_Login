from django.test import TestCase
from django.urls import reverse,resolve
from user.models import RegistrationPage
from user.forms import  Registrationform
from user.views import Registrationpage, Loginpage, Logoutpage

# Create your tests here.
class RegistrationPageModelTest(TestCase):
    @classmethod
    def setuptestdata(cls):
        cls.RegistrationPage.objects.create(
            name='admin',
            email='admin@gmail.com',
            mobile_no='12345667',
            address='delhi',
            password='admin1234'
        )
        
    # def testmodelcontent(self):
    #     self.assertEqual(self.RegistrationPage.name,'admin')
    #     self.assertEqual(self.RegistrationPage.email,'admin@gmail.com')
    #     self.assertEqual(self.RegistrationPage.mobile_no,'12345667')
    #     self.assertEqual(self.RegistrationPage.address,'delhi')
    #     self.assertEqual(self.RegistrationPage.password,'admin1234')
        
    def testurlatcorrectlocation1(self):
        response=self.client.get("/login/")
        self.assertEqual(response.status_code,200)
    def testurlatcorrectlocation2(self):
        response=self.client.get("/logout/")
        self.assertEqual(response.status_code,200)
        
        
    def testurlavailablebyname1(self):
        response=self.client.get(reverse("login"))
        self.assertEqual(response.status_code,200)
    def testurlavailablebyname2(self):
        response=self.client.get(reverse("logout"))
        self.assertEqual(response.status_code,200)
        
        
        
    def testtemplatename1correct(self):
        response=self.client.get(reverse("registration"))
        self.assertTemplateUsed(response,"registration.html")
    def testtemplatename2correct(self):
        response=self.client.get(reverse("login"))
        self.assertTemplateUsed(response,"login.html")
    def testtemplatename3correct(self):
        response=self.client.get(reverse("logout")) 
        self.assertTemplateUsed(response,"logout.html")
        
        
    def testtemplatecontain1(self):
        response=self.client.get(reverse("registration"))
        self.assertContains(response,"Register here")
    def testtemplatecontain2(self):
        response=self.client.get(reverse("login"))
        self.assertContains(response,("Login page"))
    def testtemplatecontain3(self):
        response=self.client.get(reverse("logout"))
        self.assertContains(response,("<h1>You are succesfully loggedout..!!!</h1>"))
        
     
    def testhomepage1(self):
        response=self.client.get(reverse("login"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"login.html")
        self.assertContains(response,"Login page")
        
        
    # def testname(self):
    #     registrationpage=RegistrationPage.objects.get(id=1)
    #     fieldlabel=registrationpage._meta.get_field('name').verbose_name
    #     self.assertEqual(fieldlabel,'name')
         
         
         
    def testregistrationformvalid(self):
        form=Registrationform(data={'name':"ram", 'email':"ram@gmail.com", 'mobile_no':"123456", 'address':"asdadf", 'password':"ram@123" })
        self.assertTrue(form.is_valid())
        
    
    #----------
    # def testregistrationforminvalid(self):
    #     form=Registrationform(data={'name':"sinu", 'email':"", 'mobile_no':"", 'address':"gfkjh", 'password':"" })
    #     self.assertFalse(form.is_valid())
    #---------- 
    
    
class Registrationtest(TestCase):
    def testhomeview(self):
        response=self.client.post(reverse(Registrationpage),{'name':'admin', 'email':'admin@gmail.com', 'mobile_no':'12345', 'address':'abcd', 'password':'admin@123'})
        self.assertEqual(response.status_code,302)
        self.assertEqual(RegistrationPage.objects.count(),1)
        self.assertRedirects(response, reverse('login'))
        
        
class Logintest(TestCase):
    def setup(self):
        self.loginpage=Loginpage.objects.create_loginpage(email='admin@gmail.com',password='admin@123')
    def testloginview(self):
        response=self.client.post(reverse(Loginpage),{'email':'admin@gmail.com', 'password':'admin@123'})
        self.assertEqual(response.status_code,302)
        self.assertTrue(response.url.startswith('/'))
        self.assertRedirects(response, reverse('logout'))
        
    #----------  
    # def testloginviewfailure(self):
    #     response=self.client.post(reverse(Loginpage),{'email':'wrong@gmail.com', 'password':'wrongpassword'})
    #     self.assertEqual(response.status_code,200)
    #----------   
    
    
    def testauthenticatedview(self):
        response=self.client.get(('/login'),{'email':'admin@gmail.com', 'password':'admin@123'})
        self.assertEqual(response.status_code,301)
    
    
class Logouttest(TestCase):
    def testlogouttest(self):
        response=self.client.get(reverse(Logoutpage))
        self.assertEqual(response.status_code,200)
        
        
# This is project

class Testurls(TestCase):
    #You can test if a URL can be resolved to a view function or not
    def testhomeurl(self):
        response=reverse('registration')
        self.assertEqual(resolve(response).func,Registrationpage)
        
    #You can test if the URLs patterns defined in your urls.py file are correct or not
    def testurlpattern(self):
        response=reverse('login')
        self.assertEqual(response,('/login/'))
        
    #You can test if the parameters passed in the URL are being correctly parsed and used in the view function.
    def testurlparameters(self):
        response=self.client.get(reverse('registration'))
        self.assertEqual(response.status_code,200)
    # def testurlcontains(self):
    #     response=self.client.get('register')
    #     self.assertContains(response,"result:1")
        
    #You can test if a URL is redirecting to the correct URL or not.
    def testredirecttoview(self):
        response=self.client.post(reverse(Loginpage))
        self.assertRedirects(response, reverse('logout'))
        
    #Test if a URL returns a successful response
    def test_url_success(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    def test_url_success(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)
        
    

#Test if a URL returns a specific template
    def test_url_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'login.html')
        
#

        
