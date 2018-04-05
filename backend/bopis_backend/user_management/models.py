from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        # Ensure that an email address is set
        if not email:
            raise ValueError('Users must have a valid e-mail address')

        # Ensure that a username is set

        account = self.model(
            email=self.normalize_email(email),
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password=None):
        account = self.create_user(email, password)

        account.is_admin = True
        account.save()

        return account



class General_User(AbstractBaseUser):
    # just declaring the basis of my user model 
    date_created = models.DateTimeField(blank=True, null=True , auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # objects on a custom user is lwl 
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    def __str__(self):
        return self.email

# class Profesional(General_User):
    # enterprise_name = models.CharField( null=False,  blank=False, max_length=100)
    # enterprise_location = models.CharField( null=False,  blank=False, max_length=100)
    # enterprise_website = models.URLField( default="", blank=True, max_length=100)
    # enterprise_contact = models.RegexField( regex=r'^\d{9,13}$' ,null=False,  blank=False, max_length=100)
    # enterprise_field = models.CharField( null=False,  blank=False, max_length=100)

# class Private(General_User):
    # last_name = models.CharField( default='bar'  ,   blank=False, max_length=100 )
    # first_name = models.CharField( default='foo' ,   blank=False, max_length=100 )
    # location = models.CharField( null=False,  blank=False, max_length=100)
    # website = models.URLField( default="", blank=True, max_length=100)
    # contact = models.RegexField( regex=r'^\d{9,13}$' ,null=False,  blank=False, max_length=100)
    # field = models.CharField( null=False,  blank=False, max_length=100)

# class Enterprise(General_User):


    
# Create your models here.
#2 Create your models here.
